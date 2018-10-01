from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Group

# Create your views here.


class GroupListView(ListView):
    model = Group
    paginate_by = 10
