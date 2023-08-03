from django.db import models


# Create your models here.
class MenuItem(models.Model):
    ID = models.IntegerField(primary_key=True, max_length=5)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(max_length=5)

    def get_item(self):
        return f"{self.Title} : {str(self.Price)}"

    def __str__(self):
        return self.get_item()


class Booking(models.Model):
    ID = models.IntegerField(primary_key=True, max_length=11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateField()

    def get_item(self):
        return f"{self.Name} : {str(self.BookingDate)}"

    def __str__(self):
        return self.get_item()
