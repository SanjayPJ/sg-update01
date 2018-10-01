from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Group(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk', ]
