from django.contrib import admin
from .models import TravelType, Taxi, TripSearch, Booking


@admin.register(TravelType)
class TravelTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Taxi)
class TaxiAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'taxi_type', 'driver_first_name', 'driver_last_name',
        'pickup_location', 'destination', 'passenger_capacity', 'price', 'is_active'
    )
    list_filter = ('taxi_type', 'is_active')
    search_fields = ('driver_first_name', 'driver_last_name', 'pickup_location', 'destination')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TripSearch)
class TripSearchAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pickup_location', 'destination', 'departure_datetime',
        'return_datetime', 'passenger_count', 'travel_type', 'status', 'user'
    )
    list_filter = ('travel_type', 'status')
    search_fields = ('pickup_location', 'destination', 'user__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'taxi', 'ticket_number', 'booking_code',
        'status', 'created_by_admin', 'user', 'booked_at'
    )
    list_filter = ('status', 'created_by_admin')
    search_fields = ('full_name', 'ticket_number', 'booking_code', 'mobile_number')
    readonly_fields = ('booked_at', 'updated_at')
