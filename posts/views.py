from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostCreateView(CreateView):
    model = Post
    fields = ['user', 'message', 'group', ]
