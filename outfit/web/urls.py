from django.urls import path

from outfit.web.views.outfit import HomeView, DashboardView, CreateOutfitView, EditOutfitView, \
    DeleteOutfitView, CreateOutfitPhotoView, outfit_photos, EditOutfitPhotoView, DeleteOutfitPhotoView
from outfit.web.views.weather import SunnyWeatherView, WindyWeatherView, RainyWeatherView, SnowWeatherView, \
    OtherWeatherView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('outfit/add/', CreateOutfitView.as_view(), name='create outfit'),
    path('outfit/edit/<int:pk>/', EditOutfitView.as_view(), name='edit outfit'),
    path('outfit/delete/<int:pk>/', DeleteOutfitView.as_view(), name='delete outfit'),
    path('outfit/<int:pk>/photos/', outfit_photos, name='outfit-photos'),

    path('outfitphoto/add/', CreateOutfitPhotoView.as_view(), name='create outfit-photo'),
    path('outfitphoto/edit/<int:pk>', EditOutfitPhotoView.as_view(), name='edit outfit-photo'),
    path('outfitphoto/delete/<int:pk>', DeleteOutfitPhotoView.as_view(), name='delete outfit-photo'),

    path('weather/sunny', SunnyWeatherView.as_view(), name='sunny weather'),
    path('weather/windy', WindyWeatherView.as_view(), name='windy weather'),
    path('weather/rainy', RainyWeatherView.as_view(), name='rainy weather'),
    path('weather/snow', SnowWeatherView.as_view(), name='snow weather'),
    path('weather/other', OtherWeatherView.as_view(), name='other weather'),



)
