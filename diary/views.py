from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def get_user_or_none(request):
    if request.user.is_authenticated:
        return request.user
    else:
        return None


def index(request):
    u = get_user_or_none(request)
    params = {
        'user': u,
    }
    return render(request, 'general/index.html', params)


def all_posts(request):
    u = get_user_or_none(request)
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list,
        'user': u
    }
    return render(request, 'posts/allposts.html', context)


def details(request, idx):
    u = get_user_or_none(request)
    post = get_object_or_404(Post, pk=idx)
    context = {
        'post': post,
        'user': u,
    }
    return render(request, 'posts/details.html', context)
