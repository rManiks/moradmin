from django.db import models

class Location(models.Model):
    number = models.CharField(max_length=100)
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.address_line_one

class Party(models.Model):
    forename = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.ForeignKey(Location, on_delete=models.CASCADE)

class Client(Party):
    identity_proof = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    fav_locations = models.ForeignKey(Location, on_delete=models.CASCADE) #Array

    def __str__(self):
        return self.surname

class ServiceProvier(Party):
    license_details = models.CharField(max_length=100)
    payment_details = models.CharField(max_length=100)
    insurance = models.CharField(max_length=100)
    service_geo_coverage = models.CharField(max_length=100) # Array

class BookingRequest(models.Model):
    pickup_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="trips_from")
    dropoff_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="trips_to")
    pickup_time = models.DateTimeField()
    pickup_landmark = models.CharField(max_length=100)
    estimated_distance = models.IntegerField()
    number_of_passengers = models.IntegerField()
    number_of_large_bags = models.IntegerField()

class Bid(models.Model):
    bid_by = models.ForeignKey(ServiceProvier, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    bid_notes = models.CharField(max_length=100)
    messages = models.CharField(max_length=250) # array