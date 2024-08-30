from django.urls import path

from . import views
from .views import ListingList, ListingListCategory, ListingDetailsView

urlpatterns = [
    path("api/listings/browse", ListingList.as_view(), name="api_listings_browse"),
    path("api/listings/browse/<str:category>", ListingListCategory.as_view(), name="api_listings_browse_category"),
    path("api/listings/<int:pk>", ListingDetailsView.as_view(), name="api_listings_details"),
    path("api/listings/categories", views.get_all_item_categories, name="get_all_item_categories"),
    path("api/listings/new/data", views.publish_listing, name="publish_listing"),
]