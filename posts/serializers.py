from rest_framework import serializers
from .models import Post
from django.utils.text import slugify
from authors.serializers import AuthorSerializer
from categories.serializers import CategorySerializer
from tags.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status', 'comments_count']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def validate(self, data):
        title = data.get('title', '')
        if not title.strip():
            raise serializers.ValidationError("Заголовок не должен быть пустым")
        content = data.get('content', '')
        if not content.strip():
            raise serializers.ValidationError("Контент не должен быть пустым")
        valid_statuses = ['draft', 'published', 'archived']
        status = data.get('status')
        if status and status not in valid_statuses:
            raise serializers.ValidationError("Неправильное значение статуса")
        return data

    def create(self, validated_data):
        if not validated_data.get('slug'):
            validated_data['slug'] = slugify(validated_data.get('title', ''))
        return super().create(validated_data)