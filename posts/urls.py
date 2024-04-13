from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='post_list'),
]
