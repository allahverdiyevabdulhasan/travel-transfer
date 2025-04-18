from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.home_page, name='base'),
    path('search/', search_view, name='search_view'),
    path('book/<int:taxi_id>/', book_taxi, name='book_taxi'),
]
