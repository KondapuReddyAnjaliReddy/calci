from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('home/',views.home,name='home'),
    path('hello/<str:result>/',views.hello,name='hello'),
    path('logout/',views.logoutpage,name='logout')
]
