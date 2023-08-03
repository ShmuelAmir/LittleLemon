from rest_framework import serializers

from .models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["ID", "Title", "Price", "Inventory"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["ID", "Name", "No_of_guests", "BookingDate"]
