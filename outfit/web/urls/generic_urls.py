from django.urls import path

from outfit.web.views.generic import HomeView, DashboardView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

)
