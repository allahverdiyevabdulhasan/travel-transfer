from django.shortcuts import render
from .models import *
from django.shortcuts import render
def home_page(request):
    return render(request, 'landing.html')

