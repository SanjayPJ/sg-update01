from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Group
from posts.models import Post

# Create your views here.


class GroupListView(ListView):
    model = Group
    paginate_by = 10


class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs_s = context.get('group')
        all_posts = Post.objects.filter(group=qs_s)
        paginator = Paginator(all_posts, 10)
        page = self.request.GET.get('page')
        all_post = paginator.get_page(page)
        context['all_post'] = all_post
        return context


class GroupCreateView(CreateView):
    model = Group
    fields = ['name', 'description', 'user']


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('home')


class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name', 'description', 'user']


def join(request, pk):
    add_g = get_object_or_404(Group, pk=pk)
    add_g.add_user(request.user)
    return redirect('group_detail', pk=pk)


def remove(request, pk):
    add_g = get_object_or_404(Group, pk=pk)
    add_g.remove_user(request.user)
    return redirect('group_detail', pk=pk)
