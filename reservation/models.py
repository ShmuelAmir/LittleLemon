from django.db import models


# Create your models here.
class MenuItem(models.Model):
    ID = models.IntegerField(primary_key=True, max_length=5)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return self.Title


class Booking(models.Model):
    ID = models.IntegerField(primary_key=True, max_length=11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name
