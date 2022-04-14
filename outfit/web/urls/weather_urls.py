from django.urls import path

from outfit.web.views.weather import SunnyWeatherView, WindyWeatherView, RainyWeatherView, SnowWeatherView, \
    OtherWeatherView

urlpatterns  = (
    path('sunny/', SunnyWeatherView.as_view(), name='sunny weather'),
    path('windy/', WindyWeatherView.as_view(), name='windy weather'),
    path('rainy/', RainyWeatherView.as_view(), name='rainy weather'),
    path('snow/', SnowWeatherView.as_view(), name='snow weather'),
    path('other/', OtherWeatherView.as_view(), name='other weather'),
)
