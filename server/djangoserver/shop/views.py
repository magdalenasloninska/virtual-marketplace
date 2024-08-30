from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import User, Listing
from .form import ListingForm
from .serializers import ListingSerializer


def home(request):
    cheapest_listings = Listing.objects.order_by("-price")[:5]
    output = ", ".join([listing.title for listing in cheapest_listings])
    return HttpResponse("Welcome to the shop's homepage!<br>" + output)

def new_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save()
            return redirect("/shop/browse")
    else:
        form = ListingForm()
    return render(request, "new_listing.html", {"form": form})

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

def browse(request):
    all_listings = Listing.objects.all()
    return render(request, "browse.html", {"listings": all_listings})

def profile(request, user_id):
    response = "You're looking at user profile #%s"
    return HttpResponse(response % user_id)

class ListingDetailsView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

def details(request, listing_id):
    response = "Here are the details of listing #%s"
    return HttpResponse(response % listing_id)