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
        
        print('The password is ' + password)
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
    is_active = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
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

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    # pub_date = models.DateTimeField("date published", default=datetime.now())
    category = models.CharField(
        max_length=20,
        choices=Category,
        default=Category.OTHER
    )
    photo = models.ImageField(upload_to="uploads/listings/")
    price = models.IntegerField(default=13)

    def __str__(self):
        return self.title

    def is_new(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)