from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'category', 'photo', 'price']

    def get_photo(self, obj):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url)
    
    def get_all_item_categories(self):
        return Listing.Category.choices