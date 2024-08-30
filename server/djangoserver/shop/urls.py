from django.urls import path

from . import views
from .views import ListingList, ListingListApparel, ListingListHome, ListingListOther, ListingDetailsView

urlpatterns = [
    path("api/listings/browse", ListingList.as_view(), name="api_listings_browse"),
    path("api/listings/browse/apparel", ListingListApparel.as_view(), name="api_listings_browse"),
    path("api/listings/browse/home", ListingListHome.as_view(), name="api_listings_browse"),
    path("api/listings/browse/other", ListingListOther.as_view(), name="api_listings_browse"),
    path("api/listings/<int:pk>", ListingDetailsView.as_view(), name="api_listings_details"),
    path("api/listings/categories", views.get_all_item_categories, name="get_all_item_categories"),
    path("api/listings/new/data", views.publish_listing, name="publish_listing"),
]