from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from posts.models import Comment, Group, Post, Follow
from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer,
                          GroupSerializer,
                          PostSerializer,
                          FollowSerializer)

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)
    http_method_names = ('get',)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        author_username = serializer.data.get('follower')
        print(serializer.data)
        if self.request.user.username == author_username:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        author = get_object_or_404(User, username=author_username)
        serializer.save(following=author, user=self.request.user)


# def profile_follow(request, username):
#     author = get_object_or_404(User, username=username)
#     if request.user != author:
#         Follow.objects.get_or_create(author=author, user=request.user)
#         return redirect('posts:profile', username)
#     return redirect('posts:profile', username)
#
#
#
# def profile_unfollow(request, username):
#     author = get_object_or_404(User, username=username)
#     following = request.user.follower.filter(author=author)
#     following.delete()
#     return redirect('posts:profile', username)
