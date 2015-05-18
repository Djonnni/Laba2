from django.db import models


class Passport_data(models.Model):
    surname = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    pytronymic = models.CharField(max_length=15)


class Plane(models.Model):
   # airline2 = models.ImageField()
    airline = models.CharField(max_length=20)
    privileges = models.BooleanField()
    type_of_plane = models.CharField(max_length=20)
    place_count = models.IntegerField()


class Trip(models.Model):
    point_of_departure = models.CharField(max_length=20)
    point_of_destination = models.CharField(max_length=20)
    data_of_departure = models.DateField()
    time_of_departure = models.TimeField()
    data_of_destination = models.DateField()
    time_of_destination = models.TimeField()
    plane_number = models.ForeignKey(Plane)
    cost = models.IntegerField()


class Tickets(models.Model):
    trip_number = models.ForeignKey(Trip)
    passenger_id = models.ForeignKey(Passport_data)
    ticket_id = models.IntegerField(unique=True)
    purchase_data = models.DateField()
    purchase_time = models.TimeField()
    purchase_cost = models.IntegerField()

    class Meta:
        unique_together = ('trip_number', 'passenger_id')





