from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostsView.as_view(), name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
