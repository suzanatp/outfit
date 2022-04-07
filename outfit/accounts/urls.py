
from django.urls import path

from outfit.accounts.views import UserLoginView, UserRegisterView, logout, ChangeUserPasswordView, EditProfileView, \
    ProfileDetailsView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('edit-password/',ChangeUserPasswordView.as_view(),name='change password'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/',EditProfileView.as_view(), name='edit profile'),
    path('logout/', logout, name='logout user')
)
