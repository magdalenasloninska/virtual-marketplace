from rest_framework import serializers

from .models import Listing, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'date_joined', 'about', 'profile_picture']

    def get_profile_picture(self, obj):
        request = self.context.get('request')
        profile_picture_url = obj.profile_picture.url
        return request.build_absolute_uri(profile_picture_url)

class ListingSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Listing
        fields = ['id', 'user', 'title', 'category', 'photo', 'price']

    def get_photo(self, obj):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url)
    
    def get_all_item_categories(self):
        return Listing.Category.choices
