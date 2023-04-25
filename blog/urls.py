from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home', views.home, name='home'),
    path('your_info', views.your_info, name='your_info'),
    path('sign_up', views.sign_up, name='sign_up'),
]