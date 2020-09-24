from django.db import models

# Create your models here.


locations = [
    ('Dubai','Dubai'),
    ('London','London'),
    ('Texas','Texas'),
]

hotels = [
    ('Palm','Plam'),
    ('Jumerah','Jumerah'),
    ('five','five'),
]

Guests = [
    ('adults','adults'),
    ('children','children'),
    ('infants','infants'),

] 

class Hotel(models.Model):
    hotel_name =  models.CharField(choices=hotels,max_length=30)
    location   =  models.CharField(choices=locations,max_length=30)
    check_in   =  models.DateTimeField(auto_now=False, auto_now_add=False) 
    check_out  =  models.DateTimeField(auto_now=False, auto_now_add=False) 
    guests     =  models.CharField(choices=Guests, max_length=30)

    def __str__(self):
        return self.hotel_name
