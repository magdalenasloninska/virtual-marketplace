from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Listing, CustomUser
from .form import ListingForm
from .serializers import ListingSerializer, CustomUserSerializer


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