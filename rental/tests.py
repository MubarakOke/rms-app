from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Rental, Reservation
from datetime import date, timedelta

# Create your tests here.
class RentalTestCase(TestCase):
    def setUp(self):
        Rental.objects.create(name="test rental")

    def test_index(self):
        response = self.client.get('/rental/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('reservations' in response.context)

    def test_rental_creation(self):
        rental= Rental.objects.all().count()
        self.assertEqual(rental, 1)

    def test_date_validation(self):
        rental= Rental.objects.all().first()
        yesterday_date= date.today() - timedelta(days=1)
        reservation= Reservation.objects.create(rental=rental, checkin=yesterday_date, checkout=yesterday_date)
        with self.assertRaises(ValidationError):
            reservation.full_clean()
    
    def test_checkout_date_less_than_checkin_date_validation(self):
        rental= Rental.objects.all().first()
        checkin_date= date.today() + timedelta(days=2)
        checkout_date= date.today() + timedelta(days=1)
        reservation= Reservation.objects.create(rental=rental, checkin=checkin_date, checkout=checkout_date)
        with self.assertRaises(ValidationError):
            reservation.full_clean()
        
