from datetime import datetime, timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class Listing(models.Model):

    class Category(models.TextChoices):
        APPAREL = "APPAREL", _("Apparel")
        HOME = "HOME", _("Home & lifestyle")
        OTHER = "OTHER", _("Other")

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
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