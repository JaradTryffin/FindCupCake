from django.db import models

# Create your models here.

class Measurements(models.Model):
    CAR = 'car'
    TRAIN = 'train'
    PLANE = 'PLANE'
    BUS = 'bus'

    CHOICES = (
        (CAR,'Car'),
        (TRAIN,'Train'),
        (PLANE,'Plane'),
        (BUS,'Bus'),

    )



    start_point = models.CharField(max_length=200,null=True,blank=True)
    end_point = models.CharField(max_length=200)
    type_of_transport = models.CharField(max_length=30,choices=CHOICES)
    price_per_km = models.FloatField()
    price_per_hour = models.FloatField()
    distance = models.FloatField()
    cost = models.FloatField()
    time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The distance between {self.start_point} and {self.end_point} is {self.distance} km"

