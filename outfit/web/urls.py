from django.urls import path

from outfit.web.views import show_home, create_profile

urlpatterns = (
    path('', show_home, name='show home'),
    path('create/profile/', create_profile, name='create profile'),

)
