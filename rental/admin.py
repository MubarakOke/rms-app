from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Rental, Reservation

# Register your models here.
# Register Rental on Django Admin
admin.site.register(Rental)
# Register Resevation on Django Admin
admin.site.register(Reservation)
# Unregister Group on Django Admin
admin.site.unregister(Group)
