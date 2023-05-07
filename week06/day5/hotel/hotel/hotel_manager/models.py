from django.db import models


# Create your models here.
class Hotel(models.Model):
    hotel_title = models.CharField(max_length=50),
    hotel_description = models.TextField(),
    hotel_location = models.CharField(max_length=50)
    hotel_neighbourhood = models.ForeignKey('Location', on_delete=models.CASCADE),
    hotel_images = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        return f'{hotel_title} in {hotel_location}'


class Room(models.Model):
    room_number = models.SmallIntegerField(),
    room_title = models.CharField(max_length=50),
    room_description = models.TextField(),
    room_price = models.ForeignKey('Price', on_delete=models.DO_NOTHING),
    room_images = models.ForeignKey('Image', on_delete=models.CASCADE),
    room_bookings = models.ForeignKey('Booking', on_delete=models.CASCADE)

    def __str__(self):
        return f'{room_title}'


class Booking(models.Model):
    booking_start = models.DateField(),
    booking_end = models.DateField()

    def __str__(self):
        return f'{booking_start} — {booking_end}'


class Price(models.Model):
    price_population = models.SmallIntegerField(),
    price_cost = models.DecimalField()

    def __str__(self):
        return f'{price_cost} for {price_population} persons'


class Message(models.Model):
    message_date = models.DateField(),
    message_text = models.TextField(),
    message_title = models.CharField(max_length=200),
    message_author = models.ForeignKey('User', on_delete=models.DO_NOTHING)





