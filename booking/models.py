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
