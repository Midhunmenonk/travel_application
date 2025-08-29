from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TravelOption(models.Model):
    TRAVEL_TYPES = (
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    )
    
    type = models.CharField(max_length=10, choices=TRAVEL_TYPES) 
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    available_seats = models.PositiveIntegerField() 

    def __str__(self):
        return f"{self.type} from {self.source} to {self.destination}"

    def has_available_seats(self, required_seats=1):
        """Check if the required number of seats are available"""
        return self.available_seats >= required_seats

    def get_available_seats_display(self):
        """Get a user-friendly display of available seats"""
        if self.available_seats == 0:
            return "No seats available"
        elif self.available_seats == 1:
            return "1 seat available"
        else:
            return f"{self.available_seats} seats available"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE) 
    number_of_seats = models.PositiveIntegerField() 
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed') 

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

    def get_status_display_class(self):
        """Get Bootstrap class for status display"""
        if self.status == 'Confirmed':
            return 'success'
        elif self.status == 'Cancelled':
            return 'danger'
        return 'secondary'