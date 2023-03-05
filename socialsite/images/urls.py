from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path("create/", views.image_bookmark, name="create"),
    path("post/", views.image_post, name="post"),
    path("detail/<int:id>/<slug:slug>/", views.image_detail, name="detail"),
    path("like/", views.image_like, name="like"),
    path("", views.image_list, name="list"),
    path("<int:image_id>/comment/", views.image_comment, name="post_comment"),
]
