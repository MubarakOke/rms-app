from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
 
# validate reservation date to a date from today
def validate_reservation_date(value):
    if value < date.today():
        raise ValidationError("Reservation cannot be made on past date")
    else:
        return value

# Create your models here.
# Rental Model
class Rental(models.Model):
    name= models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

# Reservation Model
class Reservation(models.Model):
    rental= models.ForeignKey(Rental, on_delete= models.SET_NULL, blank=True, null=True, related_name="reservation")
    checkin= models.DateField(blank=False, null=False, validators =[validate_reservation_date])
    checkout= models.DateField(blank=False, null=False, validators =[validate_reservation_date])

    # Validate reservation checkout date not lower than checkin date
    def clean(self):
        if self.checkout < self.checkin:
            raise ValidationError("Checkout date cannot be lower than checkin date")

    def __str__(self):
        return f"Res-{self.id}"