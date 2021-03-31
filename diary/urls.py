from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.all_posts, name='allposts'),
    path('posts/<int:pk>/', views.details, name='details'),
    path('posts/add/',
         login_required(views.PostCreateView.as_view()), name='create'),
    path('posts/<int:pk>/update/',
         login_required(views.PostUpdateView.as_view()), name='update'),
    path('posts/<int:pk>/delete/',
         login_required(views.PostDeleteView.as_view()), name='delete'),
]
