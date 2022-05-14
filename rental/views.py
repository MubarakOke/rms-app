from django.shortcuts import render
from .models import Rental, Reservation

# Create your views here.
# Landing Page View
def index(request):
    reservations= Reservation.objects.all().order_by('id')
    return render(request, 'rental/index.html', context={"reservations": reservations})