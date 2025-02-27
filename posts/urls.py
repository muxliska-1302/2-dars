from django.urls import path
from .views import PostAPIView, PostDetailAPIView
from comments.views import CommentAPIView


app_name = 'posts'

urlpatterns = [
    path('', PostAPIView.as_view(), name='posts-list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', CommentAPIView.as_view(), name='post-comments')
]