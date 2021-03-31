from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import edit
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


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


def details(request, pk):
    u = get_user_or_none(request)
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'user': u,
    }
    return render(request, 'posts/details.html', context)


class PostCreateView(edit.CreateView):
    template_name = "posts/add.html"
    form_class = PostForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class PostUpdateView(edit.UpdateView):
    model = Post
    fields = ['title', 'description']
    template_name = "posts/update.html"


class PostDeleteView(edit.DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy('allposts')
