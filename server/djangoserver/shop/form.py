from django import forms

from .models import Listing, CustomUser, Request, Wishlist, Transaction


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
        fields = ('title',
                  'description')

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ('title',)

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ()