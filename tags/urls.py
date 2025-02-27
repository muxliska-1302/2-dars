from django.urls import path
from .views import TagAPIView, TagPostsAPIView


app_name = 'tags'

urlpatterns = [
    path('', TagAPIView.as_view(), name='tags-list'),
    path('tags/<int:tag_id>/posts/', TagPostsAPIView.as_view(), name='tag-posts'),
]