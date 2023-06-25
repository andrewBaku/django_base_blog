from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/author_<str:author>', views.get_posts_by_author, name='posts_by_author'),
    path('post/new/', views.create_new_post, name='create_new_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]