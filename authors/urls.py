from django.urls import path
from .views import AuthorAPIView

app_name = 'authors'

urlpatterns = [
    path('', AuthorAPIView.as_view(), name='authors-list'),
]