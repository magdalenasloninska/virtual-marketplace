from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the shop's homepage!")

def profile(request, user_id):
    response = "You're looking at user profile #%s"
    return HttpResponse(response % user_id)

def details(request, listing_id):
    response = "Here are the details of listing #%s"
    return HttpResponse(response % listing_id)