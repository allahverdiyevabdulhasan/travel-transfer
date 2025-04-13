from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import SearchForm, BookingForm
from django.db.models import Q

def home(request):
    form = SearchForm()
    return render(request, 'landing.html', {'form': form})

def search_results(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            pickup = form.cleaned_data['pickup_location']
            destination = form.cleaned_data['destination']
            passengers = form.cleaned_data['passengers']
            flight_type = form.cleaned_data['flight_type']

            taxis = Taxi.objects.filter(
                Q(pickup_location__icontains=pickup) &
                Q(destination__icontains=destination) &
                Q(capacity__gte=passengers) &
                Q(is_available=True)
            )

            return render(request, 'results.html', {'taxis': taxis, 'form': form})

    return redirect('home')

def book_taxi(request, taxi_id):
    taxi = get_object_or_404(Taxi, id=taxi_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.taxi = taxi
            booking.flight_type = request.POST.get('flight_type')
            booking.journey_date = request.POST.get('journey_date')
            booking.return_date = request.POST.get('return_date')
            booking.passengers = request.POST.get('passengers')
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form, 'taxi': taxi})
