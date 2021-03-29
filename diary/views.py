from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    if request.user.is_authenticated:
        u = request.user
    else:
        u = None
    params = {
        'user': u,
    }
    return render(request, 'general/index.html', params)


def all_posts(request):
    if request.user.is_authenticated:
        u = request.user
    else:
        u = None
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list,
        'user': u
    }
    return render(request, 'posts/allposts.html', context)
