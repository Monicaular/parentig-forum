from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf.urls import handler500
from . import views
from .views import custom_404_page, custom_500_page

urlpatterns = [
    path("", include("posts.urls"), name="posts-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("custom500/", views.custom_500_page, name="custom500")
]


handler404 = custom_404_page
handler500 = custom_500_page