from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_post', views.new_post),
    path('posts/new', views.add_post),
    path('posts/<int:post_id>', views.one_post),
    path('add_comment/<int:post_id>', views.add_comment),
    path('search', views.search),
]
