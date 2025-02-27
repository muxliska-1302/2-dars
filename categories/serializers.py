from rest_framework import serializers
from .models import Category
from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','name', 'slug', 'description', 'posts_count']
        read_only_fields = ['id', 'slug', 'posts_count']

    def get_posts_count(self, obj):
        return obj.posts.count()

    def create(self, validated_data):
        if not validated_data.get('slug'):
            validated_data['slug'] = slugify(validated_data.get('name', ''))
        return super().create(validated_data)