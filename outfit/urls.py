from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('outfit.web.urls')),
    path('accounts/', include('outfit.accounts.urls')),
]
