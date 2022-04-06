from django.urls import path

from outfit.web.views import create_profile, HomeView, DashboardView, CreateOutfitView, EditOutfitView, \
    DeleteOutfitView, CreateOutfitPhotoView, outfit_photos, EditOutfitPhotoView, DeleteOutfitPhotoView

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

    path('create/profile/', create_profile, name='create profile'),

)
