from datetime import datetime
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=40)
    profile_picture = models.ImageField(upload_to="uploads/users/")

    def __str__(self):
        return self.username

class Listing(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    # pub_date = models.DateTimeField("date published", default=datetime.now())
    photo = models.ImageField(upload_to="uploads/listings/")
    price = models.IntegerField(default=13)

    def __str__(self):
        return self.title

    def is_new(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)