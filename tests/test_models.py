from django.test import TestCase

from reastaurant.models import MenuItem


class TestModels(TestCase):
    def test_menu_item(self):
        item = MenuItem.objects.create(ID=5, Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.Title, "IceCream")
