from rest_framework import serializers
from .models import Tag
from django.utils.text import slugify


class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'posts_count']
        read_only_fields = ['id', 'slug']

    def get_posts_count(self, obj):
        return obj.posts.count()

    def create(self, validated_data):
        if not validated_data.get('slug'):
            validated_data['slug'] = slugify(validated_data.get('name', ''))
        return super().create(validated_data)