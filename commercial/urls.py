from django.urls import path
from . import views


# for the UserFavorite we shold do a urls so the user can go to it and view there favorite offer and have 
# a button so he can click it and see if it is still available or not 


urlpatterns = [
    path('', views.index, name='index'),
    path('specialoffer/', views.specialoffer, name='specialoffer'),
    path('room/', views.room, name='room'),
    path('coffeebreak/', views.coffeebreak, name='coffeebreak'),
    path('reservation/', views.reservation, name='reservation'),
]

