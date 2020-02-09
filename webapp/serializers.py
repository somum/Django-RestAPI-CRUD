from rest_framework import serializers
from .models import flight

class flightSerializer(serializers.ModelSerializer):
    class Meta:
        model=flight
        #fields=('flight_name',)
        fields='__all__'

