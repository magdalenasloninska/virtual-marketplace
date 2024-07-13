from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("users/<int:user_id>/", views.profile, name="profile"),
    path("listings/<int:listing_id>/", views.details, name="details"),
]