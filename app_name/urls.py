from django.urls import path
from .views import home_login
urlpatterns = [
    path('login/', home_login)
]