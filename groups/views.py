from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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
