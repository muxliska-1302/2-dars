from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tag
from posts.models import Post
from django.shortcuts import get_object_or_404
from .serializers import TagSerializer
from posts.serializers import PostSerializer


class TagAPIView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagPostsAPIView(APIView):
    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, id=tag_id)
        posts = Post.objects.filter(tags=tag)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)