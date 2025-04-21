from django.urls import path
from .views import *

urlpatterns = [
    # path('', home_page, name='base'),
    path('contact/', contact_view, name='contact'),
    path('faq_list/', faq_list, name='faq_list'),
    path('about/', about_view, name='about'),
]
