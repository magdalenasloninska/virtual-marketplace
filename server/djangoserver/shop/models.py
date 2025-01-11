from datetime import date, datetime, timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, date_joined, about, profile_picture, password, **other_fields):

        if not email:
            raise ValueError(_('Email address is required!'))

        user = self.model(email=email,
                          username=username,
                          date_joined=date_joined,
                          about=about,
                          profile_picture=profile_picture,
                          **other_fields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, date_joined, about, profile_picture, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email=email,
                                username=username,
                                date_joined=date_joined,
                                about=about,
                                profile_picture=profile_picture,
                                password=password,
                                **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    username = models.CharField(max_length=120, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    about = models.TextField(max_length=400, default='Hi!')
    profile_picture = models.ImageField(upload_to='uploads/users', default='uploads/users/default_profile_pic.JPEG')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Listing(models.Model):

    class Category(models.TextChoices):
        APPAREL = "APPAREL", _("Apparel")
        HOME = "HOME", _("Home & lifestyle")
        OTHER = "OTHER", _("Other")

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=Category,
        default=Category.OTHER
    )
    photo = models.ImageField(upload_to="uploads/listings/")
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=13)
    sold = models.BooleanField(default=False)
    featured = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @classmethod
    def get_newest(cls, user_id):
        return cls.objects.filter(user=user_id).order_by('-pub_date')[:3]

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField(max_length=120)
    content = models.ManyToManyField(Listing)

class Request(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField(max_length=120)
    description = models.TextField(max_length=1000)
    listings = models.ManyToManyField(Listing)

    def linked_listings_count(self):
        return self.listings.count()

class Transaction(models.Model):

    class TransactionStatus(models.TextChoices):
        INITIATED = "INITIATED"
        AWAITING_PAYMENT = "AWAITING_PAYMENT"
        COMPLETED = "COMPLETED"
        CANCELLED = "CANCELLED"

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=TransactionStatus,
        default=TransactionStatus.INITIATED
    )

class Review(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField(max_length=400)