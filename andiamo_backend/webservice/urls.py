from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('store_locations', views.store_locations, name='store_locations'),
    path('place_order', views.place_order, name='place_order'),
]
