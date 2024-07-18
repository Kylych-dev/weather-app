from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_ts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.route')),
    path('weather/', include('apps.weather.urls')),
]

urlpatterns += doc_ts

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)