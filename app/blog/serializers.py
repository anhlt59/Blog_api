from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    """ Serializers for post object."""

    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all()
    # )

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'title', 'slug', 'content', 'status',# 'tags',
        )
        read_only_fields = ('id',)
