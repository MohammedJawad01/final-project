from django.contrib import admin
from .models import SpecialOffer, Room, CoffeeBreak, Reservation, UserFavorite, UserReservationHistory

# Register your models here.



admin.site.register(SpecialOffer)
admin.site.register(Room)
admin.site.register(CoffeeBreak)
admin.site.register(Reservation)
admin.site.register(UserFavorite)
admin.site.register(UserReservationHistory)