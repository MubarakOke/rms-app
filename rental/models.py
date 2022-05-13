from django.db import models

# Create your models here.
# Rental Model
class Rental(models.Model):
    name= models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# Reservation Model
class Reservation(models.Model):
    rental_id= models.ForeignKey(Rental, on_delete= models.SET_NULL, blank=True, null=True, related_name="rental")
    checkin= models.DateField(blank=True, null=True)
    checkout= models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Res-{self.id}"