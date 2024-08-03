from django.urls import path

from . import views
from .views import ListingList

urlpatterns = [
    path("", views.home, name="home"),
    path("browse", views.browse, name="browse"),
    path("new-listing", views.new_listing, name="new_listing"),
    path("users/<int:user_id>/", views.profile, name="profile"),
    path("listings/<int:listing_id>/", views.details, name="details"),
    path("api/browse", ListingList.as_view(), name="api_browse"),
]