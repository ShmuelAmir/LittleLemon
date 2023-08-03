from django.test import TestCase

from reastaurant.models import MenuItem


class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(ID=5, Title="IceCream", Price=80, Inventory=100)
        MenuItem.objects.create(ID=6, Title="Egg", Price=10, Inventory=100)
        MenuItem.objects.create(ID=7, Title="Bread", Price=20, Inventory=100)
        MenuItem.objects.create(ID=8, Title="Butter", Price=30, Inventory=100)

        return super().setUp()

    def test_getall(self):
        items = MenuItem.objects.all()

        # check if serializer is working
        self.assertEqual(items[0].Title, "IceCream")
        self.assertEqual(items[1].Title, "Egg")
        self.assertEqual(items[2].Title, "Bread")
        self.assertEqual(items[3].Title, "Butter")
