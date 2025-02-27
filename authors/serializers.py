from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio']
        read_only_fields = ['id']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя не должно быть пустым")
        return value
    def validate_email(self, value):
        if " " in value:
            raise serializers.ValidationError("Email не должен содержать пробелы")
        return value