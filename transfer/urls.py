from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),  # Ana sayfa (home) yolu
    path('search/', views.search_results, name='search'),  # Arama sonuçları yolu
    path('book/<int:taxi_id>/', views.book_taxi, name='book_transfer'),  # Taksi rezervasyon yolu
]
