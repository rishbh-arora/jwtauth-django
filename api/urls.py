from django.urls import path, re_path
from .views import RegisterView, LoginView, notfound
from django.shortcuts  import redirect

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]