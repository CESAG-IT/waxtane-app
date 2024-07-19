from django.urls import path

from accounts.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('signup', register_view, name="register"),
    path('signin', login_view, name="login"),
    path('signout', logout_view, name="logout"),
    path('profile', profile_view, name="profile"),
]
