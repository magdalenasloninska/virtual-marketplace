from django import forms

from .models import Listing, CustomUser, Request


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title',
                  'category',
                  'photo',
                  'description',
                  'price')

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',
                  'username',
                  'about',
                  'profile_picture',
                  'password')
        
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('title')