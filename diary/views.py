from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
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


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create_post(
                title=form.cleaned_data['title'], user=request.user, desc=form.cleaned_data['description'])
            post.save()
        return redirect("/posts")
    else:
        form = PostForm()

    return render(request, "posts/add.html", {"form": form})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'description']
    template_name = "posts/update.html"

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('details', kwargs={'pk': post_id})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy('allposts')
