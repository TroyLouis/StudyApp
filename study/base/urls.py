from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('room/', views.room, name="room"),
  path('hello/', views.hello, name="hello"),
]
