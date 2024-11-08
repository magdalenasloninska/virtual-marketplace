from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Listing, CustomUser, Request, Wishlist
from .form import ListingForm, RequestForm, WishlistForm
from .serializers import ListingSerializer, CustomUserSerializer, RequestSerializer, WishlistSerializer


def get_all_item_categories(request):
    categories = [{'text': value, 'value': key} for key, value in Listing.Category.choices]
    return JsonResponse({"categories": categories})

@csrf_exempt
def publish_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            user_id = int(form.data.get('id'))
            user = CustomUser.objects.get(id=user_id)
            listing.user = user
            listing.save()
            return JsonResponse({'message': f'New listing {listing.id} published successfully!'})
        else:
            print(form.errors)
        
    return JsonResponse({'message': 'OOPS!'})

class ListingList(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingListCategory(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer

    def get_queryset(self):
        category = self.kwargs['category'].upper()
        return Listing.objects.filter(category=category)

class ListingListOfUser(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        return Listing.objects.filter(user=user_id)

class ListingDetailsView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class UserDetailsView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

@csrf_exempt
def publish_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            request = form.save(commit=False)
            user_id = int(form.data.get('id'))
            user = CustomUser.objects.get(id=user_id)
            request.user = user
            request.save()
            return JsonResponse({'message': f'New request {request.id} published successfully!'})
        else:
            print(form.errors)
        
    return JsonResponse({'message': 'OOPS!'})

class RequestList(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestDetailsView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

@csrf_exempt
def link_listing_to_request(request, pk):
    if request.method == 'POST':
        current_request = Request.objects.get(id=pk)
        listing = Listing.objects.get(id=request.POST.get('listing_id'))
        current_request.listings.add(listing)

        return JsonResponse({'message': f'New listing linked successfully!'})

    return JsonResponse({'message': 'OOPS!'})

class WishlistList(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = WishlistSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        return Wishlist.objects.filter(user=user_id)

@csrf_exempt
def create_new_wishlist(request, pk):
    if request.method == 'POST':
        form = WishlistForm(request.POST)

        if form.is_valid():
            wishlist = form.save(commit=False)
            user = CustomUser.objects.get(id=pk)
            wishlist.user = user
            wishlist.save()
            print(wishlist.title)
            return JsonResponse({'message': f'New wishlist {wishlist.id} published successfully!'})
        else:
            print(form.errors)
        
    return JsonResponse({'message': 'OOPS!'})

@csrf_exempt
def link_listing_to_wishlist(request, pk):
    if request.method == 'POST':
        current_request = Request.objects.get(id=pk)
        listing = Listing.objects.get(id=request.POST.get('listing_id'))
        current_request.listings.add(listing)

        return JsonResponse({'message': f'New listing linked successfully!'})

    return JsonResponse({'message': 'OOPS!'})