from statistics import mean

from rest_framework import serializers
from django.db.models import Avg

from .models import \
    Listing, \
    CustomUser, \
    Request, \
    Wishlist, \
    Transaction, \
    Review


class CustomUserSerializer(serializers.ModelSerializer):
    avg_score = serializers.SerializerMethodField()
    no_of_reviews = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id',
                  'username',
                  'date_joined',
                  'about',
                  'profile_picture',
                  'avg_score',
                  'no_of_reviews']

    def get_profile_picture(self, obj):
        request = self.context.get('request')
        profile_picture_url = obj.profile_picture.url
        return request.build_absolute_uri(profile_picture_url)
    
    def get_avg_score(self, obj):
        return Review.objects.filter(recipient=obj).aggregate(Avg('stars'))['stars__avg'] or 0

    def get_no_of_reviews(self, obj):
        return Review.objects.filter(recipient=obj).count()

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
                  'price',
                  'sold',
                  'featured']

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
                  'description',
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
        
class TransactionSerializer(serializers.ModelSerializer):
    listing = ListingSerializer()

    class Meta:
        model = Transaction
        fields = ['id',
                  'listing',
                  'buyer',
                  'status']
        
class ReviewSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer()
    recipient = CustomUserSerializer()

    class Meta:
        model = Review
        fields = ['id',
                  'transaction',
                  'recipient',
                  'stars',
                  'comment']