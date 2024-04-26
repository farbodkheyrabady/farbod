from . import views
from django.urls import path

urlpatterns = [
    path("blog_list", views.blog_list, name="blog_list"),
    path("blog_det/<int:id>", views.blog_det, name="blog_det"),
    path("cate/<int:pk>", views.category, name="cate"),
]