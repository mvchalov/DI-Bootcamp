from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class Vehicle(models.Model):
    date_created = models.DateTimeField()
    real_cost = models.IntegerField(default=0)
    size = models.ForeignKey('VehicleSize', on_delete=models.DO_NOTHING)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.DO_NOTHING)


class VehicleType(models.Model):
    name = models.CharField(max_length=30)


class VehicleSize(models.Model):
    name = models.CharField(max_length=30)


class Rental(models.Model):
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    customer = models.ForeignKey('Customer', on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.DO_NOTHING)


class RentalRate(models.Model):
    daily_rate = models.IntegerField(default=0)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.DO_NOTHING)
    vehicle_size = models.ForeignKey('VehicleSize', on_delete=models.DO_NOTHING)


