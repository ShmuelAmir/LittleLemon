from django.test import TestCase

from reservation.models import MenuItem


class TestModels(TestCase):
    def test_menu_item(self):
        item = MenuItem.objects.create(ID=5, Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.Title, "IceCream")
