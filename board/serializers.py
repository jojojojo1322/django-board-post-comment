# api/serializers.py
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    user = UserSerializer(read_only=True)

    
    class Meta:
        model = Post
        fields = (
            'url',
            'user',
            'id',
            'title',
            'content',
            'comments',
            'created_at',
        )
        read_only_fields = ('created_at',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)


    class Meta:
        model = Comment
        fields = (
        'user',
        'post',
        'id',
        'content',
        )
        read_only_fields = ('created_at',)
