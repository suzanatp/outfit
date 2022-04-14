from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('outfit.web.urls.generic_urls')),
                  path('weather/', include('outfit.web.urls.weather_urls')),
                  path('outfit/', include('outfit.web.urls.outfit_urls')),
                  path('outfitphoto/', include('outfit.web.urls.outfitphoto_urls')),
                  path('accounts/', include('outfit.accounts.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
