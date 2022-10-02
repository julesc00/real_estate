from django.db import models
from django.urls import reverse


class Listing(models.Model):
    """listing object"""
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    num_bedrooms = models.PositiveIntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listings:retrieve-listing", args=[self.id])
