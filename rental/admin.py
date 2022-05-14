from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Rental, Reservation

class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'reservations')
    def reservations(self, obj):
        return [reservation for reservation in obj.reservation.all()]

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental')



# Register Rental on Django Admin
admin.site.register(Rental, RentalAdmin)
# Register Resevation on Django Admin
admin.site.register(Reservation, ReservationAdmin)
# Unregister Group on Django Admin
admin.site.unregister(Group)
