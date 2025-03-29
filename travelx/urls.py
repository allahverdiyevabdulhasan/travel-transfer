from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('account.urls')),
    path('', include('core.urls')),
    # path('', include('flight.urls')),
    # path('', include('hotel.urls')),
    # path('', include('transfer.urls')),
    # path('', include('trip.urls')),
    # path('', include('register.urls')),
    path('', include('blog.urls')),

]

# urlpatterns += i18n_patterns()



# django-admin makemessages -l en -l tr --ignore=env
# django-admin compilemessages

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

