from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

User = get_user_model()

from .forms import SignUpForm
from posts.models import Post

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def post_user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    post_lists = Post.objects.filter(user__in=[user])
    paginator = Paginator(post_lists, 10)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    context = {
        'post_list': post_list,
        'author': user,
    }
    return render(request, 'accounts/user.html', context)
