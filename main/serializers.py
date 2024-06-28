from rest_framework import serializers
from .models import Category, Tag, Author, Post, About, Extra_Info, HappyClients, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'tags', 'author', 'category', 'body', 'comment_set', 'created_at',
                  'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class Extra_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_Info
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    extra_info = Extra_InfoSerializer(read_only=True)

    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
