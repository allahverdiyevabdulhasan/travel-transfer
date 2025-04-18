from django.db import models
from django.contrib.auth.models import User


# 1. Səyahət Tipi (One-way / Return)
class TravelType(models.Model):
    name = models.CharField(max_length=20, unique=True)  # One-way və ya Return

    def __str__(self):
        return self.name


# 2. Taksi Modeli
class Taxi(models.Model):
    TYPE_CHOICES = [
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('van', 'Van'),
    ]

    taxi_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    driver_first_name = models.CharField(max_length=50)
    driver_last_name = models.CharField(max_length=50)
    
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    passenger_capacity = models.PositiveIntegerField()
    luggage_capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_return_price = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='taxi_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_taxi_type_display()} - {self.driver_first_name} {self.driver_last_name}"


# 3. Axtarış Məlumatları (İstifadəçi tərəfindən formda göndərilir)
class TripSearch(models.Model):
    travel_type = models.ForeignKey(TravelType, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_datetime = models.DateTimeField()
    return_datetime = models.DateTimeField(null=True, blank=True)
    passenger_count = models.PositiveIntegerField()
    user_ip = models.GenericIPAddressField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed')],
        default='pending'
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pickup_location} → {self.destination} ({self.travel_type})"


# 4. Rezervasiya Modeli
class Booking(models.Model):
    trip_search = models.ForeignKey(TripSearch, on_delete=models.CASCADE)
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    ticket_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    contact_preference = models.CharField(max_length=100)  # WhatsApp və ya Gmail
    booking_code = models.CharField(max_length=20, unique=True)
    note = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )
    created_by_admin = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    booked_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.full_name} for {self.taxi} - {self.booking_code}"
