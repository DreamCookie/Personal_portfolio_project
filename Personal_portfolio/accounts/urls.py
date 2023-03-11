from django.urls import path
from .views import registration_view, login_view
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', registration_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
