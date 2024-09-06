from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics

from .models import Listing, CustomUser
from .form import ListingForm, CustomUserForm
from .serializers import ListingSerializer, CustomUserSerializer


def get_all_item_categories(request):
    categories = [{'text': value, 'value': key} for key, value in Listing.Category.choices]
    return JsonResponse({"categories": categories})

@csrf_exempt
def publish_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save()
            return JsonResponse({'message': f'New listing {listing.id} published successfully!'})
        else:
            print(form.errors)
        
    return JsonResponse({'message': 'OOPS!'})

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingListCategory(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        category = self.kwargs['category'].upper()
        return Listing.objects.filter(category=category)

class ListingDetailsView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            user = authenticate(request=request,
                                email=email,
                                password=password)
            
            if user is not None:
                login(request, user)
            else:
                # TODO: implement some kind of notification system
                pass

class UserDetailsView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer