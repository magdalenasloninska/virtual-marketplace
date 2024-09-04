from django.contrib import admin

from .models import CustomUser, Listing


admin.site.register(CustomUser)
admin.site.register(Listing)