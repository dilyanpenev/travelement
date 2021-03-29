from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return render(request, 'general/index.html')


def all_posts(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/allposts.html', context)
