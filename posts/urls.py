from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("posts/", views.PostsView.as_view(), name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:pk>/", views.edit_post, name="edit_post"),
    path("<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("like_post/<int:post_id>/", views.like_post, name="like_post"),
    path("rules/", views.rules_view, name="rules"),
    path("resources/", views.resources, name="resources"),
    path("contact/", views.contact_us, name="contact"),
    path("like_comment/<int:comment_id>/", views.like_comment, name="like_comment"),
    path(
        "<int:pk>/edit_comment/<int:comment_id>/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "<int:pk>/delete_comment/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
]
