from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # login/logout
    # path("login/", views.user_login, name="login")
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # # change password
    # path(
    #     "password_change/",
    #     auth_views.PasswordChangeView.as_view(),
    #     name="password_change",
    # ),
    # path(
    #     "password_change/done/",
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # # reset password urls
    # path(
    #     "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    # ),
    # path(
    #     "password_reset/done/",
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password_reset/<uidb64>/<token>",
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password_reset/complete/",
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
    path("", include("django.contrib.auth.urls")),
    # regiter
    path("register/", views.register, name="register"),
    # dashboard
    path("", views.dashboard, name="dashboard"),
    # edit
    path("edit/", views.edit, name="edit"),
    # users
    path("users/", views.user_list, name="user_list"),
    path("users/follow", views.user_follow, name="user_follow"),
    path("users/<username>/", views.user_detail, name="user_detail"),
]
