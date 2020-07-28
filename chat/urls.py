from django.urls import path
from . import views

urlpatterns = [
    path('', views.Account_login.as_view(), name='login'),
    path('<str:room_name>/', views.room, name='room'),
]