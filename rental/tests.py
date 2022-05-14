from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Rental, Reservation
from datetime import date, timedelta

# Create your tests here.
class RentalTestCase(TestCase):
    # set up rentals for reservations 
    def setUp(self):
        Rental.objects.create(name="test rental")

    # test successful page loading
    def test_index(self):
        response = self.client.get('/rental/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('reservations' in response.context)

    # test succssful creation of rental 
    def test_rental_creation(self):
        rental= Rental.objects.all().count()
        self.assertEqual(rental, 1)

    # test to ensure reservation date is not less than today
    def test_date_validation(self):
        rental= Rental.objects.all().first()
        yesterday_date= date.today() - timedelta(days=1)
        reservation= Reservation.objects.create(rental=rental, checkin=yesterday_date, checkout=yesterday_date)
        with self.assertRaises(ValidationError):
            reservation.full_clean()

    # test to ensure checkout date is not less than checkin date
    def test_checkout_date_less_than_checkin_date_validation(self):
        rental= Rental.objects.all().first()
        checkin_date= date.today() + timedelta(days=2)
        checkout_date= date.today() + timedelta(days=1)
        reservation= Reservation.objects.create(rental=rental, checkin=checkin_date, checkout=checkout_date)
        with self.assertRaises(ValidationError):
            reservation.full_clean()

    # test successful creation of reservation
    def test_reservation_creation(self):
        rental= Rental.objects.all().first()
        checkin_date= date.today() + timedelta(days=2)
        checkout_date= date.today() + timedelta(days=2)
        reservation= Reservation.objects.create(rental=rental, checkin=checkin_date, checkout=checkout_date)
        reservation_count= Reservation.objects.count()
        self.assertEqual(reservation_count, 1)
        
    # test reservations of same rental, present item's previous id equal to previous item's id
    def test_present_item_previous_rental_id_equal_to_previous_item_id(self):
        rental= Rental.objects.all().first()
        checkin_date= date.today() + timedelta(days=2)
        checkout_date= date.today() + timedelta(days=2)
        checkout_date_1= date.today() + timedelta(days=5)
        Reservation.objects.create(rental=rental, checkin=checkin_date, checkout=checkout_date)
        Reservation.objects.create(rental=rental, checkin=checkin_date, checkout=checkout_date_1)
        first= Reservation.objects.filter(rental=rental).first()
        last= Reservation.objects.filter(rental=rental).last()
        reservation_count= Reservation.objects.count()
        self.assertEqual(reservation_count, 2)
        self.assertEqual(last.previous_id, first.id)

        
