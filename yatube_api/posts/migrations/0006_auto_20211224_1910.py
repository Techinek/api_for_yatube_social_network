# Generated by Django 2.2.16 on 2021-12-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20211224_1839'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_subscription',
        ),
    ]
