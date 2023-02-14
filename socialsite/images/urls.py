from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path("create/", views.image_bookmark, name="create"),
    path("post/", views.image_post, name="post"),
]
