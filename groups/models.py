from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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

    def add_user(self, add_u):
        self.user.add(add_u)
        self.save()

    def remove_user(self, add_u):
        self.user.remove(add_u)
        self.save()

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'pk': self.pk})
