from django.http import HttpResponse
from django.shortcuts import render, redirect
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

def publish_listing(request):
    if request.method == 'POST':
        form = request.data
        title = form.get('title')
        price = format.get('price')

        new_listing = Listing.objects.create(title=title, price=price)
        
        

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all()
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