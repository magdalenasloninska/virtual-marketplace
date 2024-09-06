from django import forms

from .models import Listing, CustomUser


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'category', 'photo', 'price')

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'date_joined', 'about', 'profile_picture')