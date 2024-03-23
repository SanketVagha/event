from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.id

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()  # Ensure this line is present
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.id)