from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.all_posts, name='allposts'),
    path('posts/<int:idx>/', views.details, name='details'),
    path('posts/add/', views.create_post, name='create'),
    path('posts/<int:idx>/update/',
         login_required(views.PostUpdateView.as_view()), name='update'),
]
