from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.all_posts, name='allposts'),
    path('posts/<int:idx>/', views.details, name='details'),
    path('posts/add/', views.create_post, name='create')
]
