from django.urls import path
from .views import CategoryAPIView, CategoryPostsAPIView


app_name = 'categories'

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories-list'),
    path('categories/<int:category_id>/posts/', CategoryPostsAPIView.as_view(), name='category-posts'),
]