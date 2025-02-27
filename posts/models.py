from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('tags.Tag', related_name='posts')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title