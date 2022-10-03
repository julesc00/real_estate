from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import ListingForm
from .models import Listing


def list_listings(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "index.html", context)


def retrieve_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


def create_listing(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listings:list-listings")
    context = {"form": form}
    return render(request, "create_listing.html", context)


def update_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listings:list-listings")
    context = {
        "listing": listing,
        "form": form
    }
    return render(request, "update_listing.html", context)


def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    listing.delete()
    return redirect("listings:list-listings")
