from django.urls import path

from outfit.web.views.photo import DetailsPhotoView, like_outfit_photo, dislike_outfit_photo, \
    CreateOutfitPhotoView, EditOutfitPhotoView, DeleteOutfitPhotoView

urlpatterns = (path('details/<int:pk>/', DetailsPhotoView.as_view(), name='details photo'),
               path('like/<int:pk>/', like_outfit_photo, name='like outfit photo'),
               path('dislike/<int:pk>/', dislike_outfit_photo, name='dislike outfit photo'),
               path('add/', CreateOutfitPhotoView.as_view(), name='create outfit-photo'),
               path('edit/<int:pk>/', EditOutfitPhotoView.as_view(), name='edit outfit-photo'),
               path('delete/<int:pk>/', DeleteOutfitPhotoView.as_view(), name='delete outfit-photo'),)
