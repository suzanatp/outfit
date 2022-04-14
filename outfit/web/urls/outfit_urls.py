from django.urls import path

from outfit.web.views.outfit import CreateOutfitView, EditOutfitView, \
    DeleteOutfitView, DetailsOutfitView, comment_outfit, delete_comment
from outfit.web.views.photo import outfit_photos

urlpatterns = (
    path('add/', CreateOutfitView.as_view(), name='create outfit'),
    path('details/<int:pk>/', DetailsOutfitView.as_view(), name='details outfit'),
    path('comment/<int:pk>/', comment_outfit, name='comment outfit'),
    path('comment-delete/<int:outfit_pk>/<int:comment_pk>/', delete_comment, name="delete comment"),
    path('edit/<int:pk>/', EditOutfitView.as_view(), name='edit outfit'),
    path('delete/<int:pk>/', DeleteOutfitView.as_view(), name='delete outfit'),
    path('<int:pk>/photos/', outfit_photos, name='outfit-photos'),
)
