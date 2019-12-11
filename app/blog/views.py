from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from core.models import Post
from blog import serializers


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     """Retrieve the recipes for the authenticated user"""
    #     return self.queryset.filter(user=self.request.user)

    # def get_serializer_class(self):
    #     """Return appropriate serializer class"""
    #     if self.action == 'retrieve':
    #         return serializers.RecipeDetailSerializer
    #
    #
    # def perform_create(self, serializer):
    #     """Create a new recipe"""
    #     serializer.save(user=self.request.user)
