from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='base'),
    path('contact/', contact_view, name='contact'),
]
