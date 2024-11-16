from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views, auth
from .views import \
    ListingList, \
    ListingListCategory, \
    ListingListOfUser, \
    ListingDetailsView, \
    UserDetailsView, \
    RequestList, \
    RequestDetailsView, \
    WishlistList, \
    WishlistDetailsView

urlpatterns = [
    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Listing-focused
    path("api/listings/browse", ListingList.as_view(), name="api_listings_browse"),
    path("api/listings/browse/<str:category>", ListingListCategory.as_view(), name="api_listings_browse_category"),
    path("api/listings/<int:pk>", ListingDetailsView.as_view(), name="api_listings_details"),
    path("api/listings/categories", views.get_all_item_categories, name="get_all_item_categories"),
    path("api/listings/new/data", views.publish_listing, name="publish_listing"),
    path("api/listings/requests/new/data", views.publish_request, name="publish_request"),
    path("api/listings/requests/all", RequestList.as_view(), name="all_requests"),
    path("api/listings/requests/<int:pk>", RequestDetailsView.as_view(), name="api_request_details"),
    path("api/listings/requests/<int:pk>/new/data", views.link_listing_to_request, name="link_listing_to_request"),

    # Transactions
    # path("api/transactions/<int:pk>/status", views.create_transaction, name="transaction_status"),
    path("api/transactions/new/data", views.create_transaction, name="new_transaction"),
    
    # User-focused
    path("api/users/register/data", auth.sign_up, name='register'),
    path("api/users/login/data", auth.login_custom_user),
    path("api/users/current-user", auth.get_current_user, name='current_user'),
    path("api/users/<int:pk>", UserDetailsView.as_view()),
    path("api/users/<int:pk>/edit/data", auth.edit_custom_user),
    path("api/users/<int:pk>/listings", ListingListOfUser.as_view()),
    path("api/users/<int:pk>/wishlists", WishlistList.as_view()),
    path("api/users/<int:pk>/wishlists/new/data", views.create_new_wishlist, name="new_wishlist"),
    path("api/wishlists/delete/<int:pk>", views.delete_wishlist, name='delete_wishlist'),
    path("api/wishlists/<int:pk>", WishlistDetailsView.as_view()),
    path("api/wishlists/<int:pk>/new/data", views.link_listing_to_wishlist, name="link_listing_to_wishlist"),
]