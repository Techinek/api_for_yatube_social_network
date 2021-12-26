from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="username", read_only=True,)
    following = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Follow
        fields = "__all__"

    def validate(self, data):
        local_user = self.context.get("request").user
        following = self.initial_data.get("following")

        if not following:
            raise serializers.ValidationError(
                detail="No data provided",
                code=status.HTTP_400_BAD_REQUEST,
            )

        author = get_object_or_404(User, username=following)

        if local_user == author:
            raise serializers.ValidationError(
                detail="User can't follow himself",
                code=status.HTTP_400_BAD_REQUEST,
            )

        if Follow.objects.filter(following=author,
                                 user=local_user).exists():
            raise serializers.ValidationError(
                detail="User can't follow same author twice",
                code=status.HTTP_400_BAD_REQUEST,
            )
        return data
