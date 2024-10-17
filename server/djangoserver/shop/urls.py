from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views, auth
from .views import \
    ListingList, \
    ListingListCategory, \
    ListingListOfUser, \
    ListingDetailsView, \
    UserDetailsView

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
    
    # User-focused
    path("api/users/register/data", auth.sign_up, name='register'),
    path("api/users/login/data", auth.login_custom_user),
    path("api/users/current-user", auth.get_current_user, name='current_user'),
    path("api/users/<int:pk>", UserDetailsView.as_view()),
    path("api/users/<int:pk>/listings", ListingListOfUser.as_view()),
]