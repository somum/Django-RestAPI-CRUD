from django.db import models

# Create your models here.

class flight(models.Model):
        flight_name=models.CharField(max_length=20)
        flight_destination=models.CharField(max_length=20)
        flight_price=models.CharField(max_length=20)

        def __str__(self):
            return self.flight_name