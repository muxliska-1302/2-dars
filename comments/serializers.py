from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'replies']
        read_only_fields = ['id', 'created_at']

    def get_replies(self, obj):
        serializer = CommentSerializer(obj.replies.all(), many=True)
        return serializer.data

    def validate_author_email(self, value):
        if " " in value:
            raise serializers.ValidationError("Email не должен содержать пробелы")
        return value

    def validate(self, data):
        parent = data.get('parent_comment')
        if parent:
            level = 1
            current = parent
            while current.parent_comment:
                level += 1
                current = current.parent_comment
            if level + 1 > 3:
                raise serializers.ValidationError("Максимально допустимый уровень вложенности комментариев - 3")
        return data