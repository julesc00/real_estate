from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import list_listings, retrieve_listing, create_listing, update_listing, delete_listing

app_name = "listings"

urlpatterns = [
    path("", list_listings, name="list-listings"),
    path("<int:id>", retrieve_listing, name="retrieve-listing"),
    path("create_listing/", create_listing, name="create-listing"),
    path("<int:id>/edit/", update_listing, name="update-listing"),
    path("<int:id>/delete/", delete_listing, name="delete-listing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
