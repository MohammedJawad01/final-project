from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import SpecialOffer, Room, CoffeeBreak, Reservation
# Create your views here.

def index(request):
    return render(request,('index.html'))


def specialoffer(request):
    special_offers = SpecialOffer.objects.all()
    return render(request,('specialoffer.html'),{
        'special_offers': special_offers
    })

def room(request):
    rooms = Room.objects.all()
    return render(request,('room.html'),{
        'rooms': rooms
        })


def coffeebreak(request):
    coffeebreaks = CoffeeBreak.objects.all()
    return render(request,('coffeebreak.html'),{
        'coffeebreaks':coffeebreaks
    })



def reservation(request):
    rooms = Room.objects.all()
    coffee_breaks = CoffeeBreak.objects.all()
    context = {
        'rooms': rooms,
        'coffee_breaks': coffee_breaks,
    }
    if request.method == 'POST':
        event_space_id = request.POST['event_space']
        coffee_break_id = request.POST['coffee_break']
        event_space = request.POST.get('event_space')
        coffee_break = request.POST.get('coffee_break')
        date_and_time = request.POST.get('date_and_time')
        number_of_attendees = request.POST.get('number_of_attendees')
        notes = request.POST.get('notes')
        event_space = Room.objects.get(pk=event_space_id)
        coffee_break = CoffeeBreak.objects.get(pk=coffee_break_id)
        # Create a new reservation instance and save it
        reservation = Reservation(
            event_space=event_space,
            coffee_break=coffee_break,
            date_and_time=date_and_time,
            number_of_attendees=number_of_attendees,
            notes=notes
        )
        reservation.save()
    return render(request, 'reservation.html',context)


# for the UserFavorite we shold do a urls so the user can go to it and view there favorite offer and have 
# a button so he can click it and see if it is still available or not 