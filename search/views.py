from django.shortcuts import render
from groups.models import Group
from posts.models import Post

# Create your views here.


def search(request):
    q = request.GET.get('q', None)
    if q is None:
        queryset = Group.objects.all()[:10]
    else:
        queryset = Group.objects.filter(name__contains=q)[:10]
    if q is None:
        queryset2 = Post.objects.all()[:10]
    else:
        queryset2 = Post.objects.filter(message__contains=q)[:10]
    context = {
        "group_list": queryset,
        "post_list": queryset2,
    }

    return render(request, "search/search.html", context)
