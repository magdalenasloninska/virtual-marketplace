from rest_framework import serializers
from django.db.models import Count

from .models import Listing, CustomUser, Request, Wishlist


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',
                  'username',
                  'date_joined',
                  'about',
                  'profile_picture']

    def get_profile_picture(self, obj):
        request = self.context.get('request')
        profile_picture_url = obj.profile_picture.url
        return request.build_absolute_uri(profile_picture_url)

class ListingSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Listing
        fields = ['id',
                  'user',
                  'title',
                  'category',
                  'photo',
                  'description',
                  'price']

    def get_photo(self, obj):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url)
    
    def get_all_item_categories(self):
        return Listing.Category.choices

class RequestSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    listings = ListingSerializer(many=True)
    linked_listings_count = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['id',
                  'user',
                  'title',
                  'listings',
                  'linked_listings_count']
        
    def get_linked_listings_count(self, obj):
        return obj.linked_listings_count()
        
class WishlistSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    content = ListingSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id',
                  'user',
                  'title',
                  'content']