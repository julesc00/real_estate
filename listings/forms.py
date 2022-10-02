from django.forms import ModelForm

from .models import Listing


class ListingForm(ModelForm):
    """Form for the listing object"""
    class Meta:
        model = Listing
        fields = (
            "title",
            "price",
            "num_bedrooms",
            "square_footage",
            "address",
        )
