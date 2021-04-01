from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import edit, DetailView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from .forms import PostForm
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


class PostListView(ListView):
    template_name = "posts/allposts.html"
    queryset = Post.objects.all()
    context_object_name = 'posts_list'

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['user'] = get_user_or_none(self.request)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['user'] = get_user_or_none(self.request)
        return context


class PostCreateView(edit.CreateView):
    template_name = "posts/add.html"
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class PostUpdateView(edit.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/update.html"

    def get_object(self):
        obj = super(PostUpdateView, self).get_object()
        if obj.user != self.request.user:
            raise Http404('You are not the author of this post.')
        return obj

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PostUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class PostDeleteView(edit.DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy('allposts')

    def get_object(self):
        obj = super(PostDeleteView, self).get_object()
        if obj.user != self.request.user:
            raise Http404('You are not the author of this post.')
        return obj
