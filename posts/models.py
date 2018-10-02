from django.db import models
from django.contrib.auth.models import User
from groups.models import Group
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-pk', ]

    def get_absolute_url(self):
        return reverse('post_list')
