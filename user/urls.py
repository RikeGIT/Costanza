from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('api/v1/register/', RegisterView.as_view(), name='api_register'),
    path('api/v1/login/', LoginView.as_view(), name='api_login'),
]