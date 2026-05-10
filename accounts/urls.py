from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import AccountRegister


urlpatterns = [
    path('register/', AccountRegister.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
