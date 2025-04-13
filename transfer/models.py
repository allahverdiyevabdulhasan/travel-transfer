from django.db import models
from django.utils import timezone

class Taxi(models.Model):
    name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    car_type = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    one_way_price = models.DecimalField(max_digits=10, decimal_places=2)
    return_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.car_type}"

class Booking(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    journey_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    passengers = models.PositiveIntegerField(default=1)
    flight_type = models.CharField(max_length=10, choices=[('oneway', 'One Way'), ('return', 'Return')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.full_name} - {self.taxi.name}"
