from django.shortcuts import render
from .models import Rental, Reservation

# Create your views here.
# Landing Page View
def index(request):
    if request.method == 'GET':
        reservations= Reservation.objects.order_by('id')
        reservations_dict= {reservations: reservations}
        return render(request, 'rental/index.html', context=reservations_dict)