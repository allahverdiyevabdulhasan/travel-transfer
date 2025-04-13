from django.contrib import admin
from .models import Taxi, Booking


@admin.register(Taxi)
class TaxiAdmin(admin.ModelAdmin):
    list_display = ('name', 'driver_name', 'car_type', 'pickup_location', 'destination', 'capacity', 'is_available')
    list_filter = ('pickup_location', 'destination', 'is_available')
    search_fields = ('name', 'driver_name', 'car_type', 'pickup_location', 'destination')
    list_editable = ('is_available',)
    ordering = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'taxi', 'journey_date', 'return_date', 'passengers', 'flight_type', 'created_at')
    list_filter = ('flight_type', 'journey_date', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number', 'taxi__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
