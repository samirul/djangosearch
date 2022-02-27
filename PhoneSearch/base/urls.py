from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('phones/<str:pk>/', views.phoneInfo, name="phones"),
    path('test/', views.test, name="test")
]
