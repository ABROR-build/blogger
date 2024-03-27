from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    text = models.TextField()
    summary = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_home_detailed_view', args=[str(self.pk)])