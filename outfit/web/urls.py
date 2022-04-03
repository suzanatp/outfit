from django.urls import path

from outfit.web.views import create_profile, HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='show home'),
    path('create/profile/', create_profile, name='create profile'),

)
