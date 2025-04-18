from django.shortcuts import render, get_object_or_404, redirect
from .models import TripSearch, Taxi, Booking, TravelType
from datetime import datetime
import uuid


def home_page(request):
    return render(request, 'search.html')


def generate_booking_code():
    return uuid.uuid4().hex[:10].upper()


def search_view(request):
    taxis = []

    if request.method == 'GET':
        pickup = request.GET.get('pickup_location')
        destination = request.GET.get('destination')
        departure = request.GET.get('departure_date')
        return_date = request.GET.get('return_date')
        passenger_count = request.GET.get('passenger_count')
        trip_type = request.GET.get('trip_type', 'oneway')

        if pickup and destination and departure and passenger_count:
            try:
                departure_dt = datetime.strptime(departure, '%Y-%m-%dT%H:%M')
                return_dt = (
                    datetime.strptime(return_date, '%Y-%m-%dT%H:%M')
                    if return_date else None
                )
                passenger_count = int(passenger_count)
            except (ValueError, TypeError):
                return render(request, 'search.html', {
                    'error': 'Zəhmət olmasa, bütün məlumatları düzgün formatda daxil edin.'
                })

            travel_type_obj, _ = TravelType.objects.get_or_create(
                name__iexact=trip_type.capitalize(),
                defaults={'name': trip_type.capitalize()}
            )

            trip = TripSearch.objects.create(
                travel_type=travel_type_obj,
                pickup_location=pickup,
                destination=destination,
                departure_datetime=departure_dt,
                return_datetime=return_dt,
                passenger_count=passenger_count,
                user_ip=request.META.get('REMOTE_ADDR'),
                user=request.user if request.user.is_authenticated else None
            )
            request.session['trip_id'] = trip.id

            taxis = Taxi.objects.filter(
                pickup_location__iexact=pickup,
                destination__iexact=destination,
                passenger_capacity__gte=passenger_count,
                is_active=True
            )

    return render(request, 'search.html', {
        'taxis': taxis
    })


def book_taxi(request, taxi_id):
    taxi = get_object_or_404(Taxi, id=taxi_id)
    trip_id = request.session.get('trip_id')

    if not trip_id:
        return redirect('home_page')

    trip = get_object_or_404(TripSearch, id=trip_id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        ticket_number = request.POST.get('ticket_number')
        mobile_number = request.POST.get('mobile_number')
        contact_preference = request.POST.get('contact_preference')
        note = request.POST.get('note')

        booking = Booking.objects.create(
            trip_search=trip,
            taxi=taxi,
            full_name=full_name,
            ticket_number=ticket_number,
            mobile_number=mobile_number,
            contact_preference=contact_preference,
            note=note,
            booking_code=generate_booking_code(),
            user=request.user if request.user.is_authenticated else None
        )

        taxi.is_active = False
        taxi.save()

        return render(request, 'booking_success.html', {'booking': booking})

    return render(request, 'book_now.html', {
        'taxi': taxi,
        'trip': trip
    })
