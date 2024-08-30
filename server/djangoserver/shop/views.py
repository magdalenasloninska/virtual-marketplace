from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import Listing
from .form import ListingForm
from .serializers import ListingSerializer


def get_all_item_categories(request):
    categories = [{'text': value, 'value': key} for key, value in Listing.Category.choices]
    return JsonResponse({"categories": categories})

@csrf_exempt
def publish_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            listing = form.save()
            return JsonResponse({'message': f'New listing {listing.id} published successfully!'})
        else:
            print(form.errors)
        
    return JsonResponse({'message': 'OOPS!'})

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingListApparel(generics.ListAPIView):
    queryset = Listing.objects.filter(category=Listing.Category.APPAREL)
    serializer_class = ListingSerializer

class ListingListHome(generics.ListAPIView):
    queryset = Listing.objects.filter(category=Listing.Category.HOME)
    serializer_class = ListingSerializer

class ListingListOther(generics.ListAPIView):
    queryset = Listing.objects.filter(category=Listing.Category.OTHER)
    serializer_class = ListingSerializer

class ListingDetailsView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
