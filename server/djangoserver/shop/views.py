from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Listing, CustomUser, Request, Wishlist, Transaction, Review
from .form import ListingForm, RequestForm, WishlistForm, TransactionForm, ReviewForm
from .serializers import \
    ListingSerializer, \
    CustomUserSerializer, \
    RequestSerializer, \
    WishlistSerializer, \
    ReviewSerializer, \
    TransactionSerializer


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
            return JsonResponse({
                'success': True,
                'message': f'New listing {listing.id} published successfully!'
            })
        else:
            print(form.errors)
        
    return JsonResponse({
        'success': False,
        'message': 'OOPS!'
    })

class ListingList(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Listing.objects.all().order_by('-pub_date')
    serializer_class = ListingSerializer

class ListingListCategory(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer

    def get_queryset(self):
        category = self.kwargs['category'].upper()
        return Listing.objects.filter(category=category).order_by('-pub_date')

class ListingListOfUser(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        return Listing.objects.filter(user=user_id).order_by('-pub_date')

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

class FeaturedListingsOfUser(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        return Listing.objects.filter(user=user_id).exclude(featured=0).order_by('featured')

@csrf_exempt
def choose_featured(request, pk):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        position = request.POST.get('position')

        old_featured = Listing.objects.filter(featured=position).filter(user=pk).first()
        
        if old_featured:
            old_featured.featured = 0
            old_featured.save()

        listing = Listing.objects.get(id=listing_id)
        listing.featured = position
        listing.save()

        return JsonResponse({
            'success': True,
            'message': f'New featured listing at {position} set!'
        })
        
    return JsonResponse({
        'success': False,
        'message': 'Error while setting a new featured listing'
    })

@csrf_exempt
def publish_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            new_request = form.save(commit=False)
            user_id = int(form.data.get('id'))
            user = CustomUser.objects.get(id=user_id)
            new_request.user = user
            new_request.save()

            return JsonResponse({
                'success': True,
                'message': f'New request {new_request.id} published successfully!'
            })
        else:
            print(form.errors)
         
    return JsonResponse({
        'success': False,
        'message': 'OOPS!'
    })

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
    
class WishlistDetailsView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

@csrf_exempt
def create_new_wishlist(request, pk):
    if request.method == 'POST':
        form = WishlistForm(request.POST)

        if form.is_valid():
            wishlist = form.save(commit=False)
            user = CustomUser.objects.get(id=pk)
            wishlist.user = user
            wishlist.save()
            return JsonResponse({'message': f'New wishlist {wishlist.id} published successfully!'})
        else:
            print(form.errors)
        
    return JsonResponse({'message': 'OOPS!'})

@csrf_exempt
def link_listing_to_wishlist(request, pk):
    if request.method == 'POST':
        wishlist = Wishlist.objects.get(id=pk)
        listing = Listing.objects.get(id=request.POST.get('listing_id'))
        wishlist.content.add(listing)

        return JsonResponse({'message': f'New listing linked successfully!'})

    return JsonResponse({'message': 'OOPS!'})

@csrf_exempt
def delete_wishlist(request, pk):
    if request.method == 'POST':
        Wishlist.objects.filter(id=pk).delete()

    return JsonResponse({'message': 'OOPS!'})

@csrf_exempt
def create_transaction(request):
    # Here's where transactions would be initialized
    # Later at a confirmation step, we would switch it to COMPLETED (?)
    # All of this would lead up to the possibility of adding a review

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)

            listing = Listing.objects.get(id=request.POST.get('listing_id'))
            listing.sold = True
            listing.save()

            buyer = CustomUser.objects.get(id=request.POST.get('buyer_id'))

            transaction.listing = listing
            transaction.buyer = buyer
            transaction.status = Transaction.TransactionStatus.COMPLETED
            transaction.save()

            return JsonResponse({
                'success': True,
                'message': 'New transaction initialized successfully!'
            })
        
    return JsonResponse({
        'success': False,
        'message': 'Error while creating a new transaction'
    })

class OrderDetailsView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class OrderListOfUser(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        return Transaction.objects.filter(buyer=user_id)

@csrf_exempt
def edit_review(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        try:
            review = Review.objects.get(transaction_id=pk)
            review.stars = request.POST.get('stars')
            review.comment = request.POST.get('comment')
            review.save()

        except Review.DoesNotExist:
            if form.is_valid():
                new_review = form.save(commit=False)
                transaction = Transaction.objects.get(id=pk)
                new_review.transaction = transaction
                new_review.recipient = transaction.listing.user
                new_review.save()

        return JsonResponse({
            'success': True,
            'message': f'New review has been published successfully!'
        })
        
    return JsonResponse({
        'success': False,
        'message': 'OOPS!'
    })


class ReviewDetailsFromOrderView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        order_id = int(self.kwargs['pk'])
        return Review.objects.filter(transaction__listing__id=order_id)

class ReviewListOfUser(generics.ListAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        return Review.objects.filter(recipient=user_id)