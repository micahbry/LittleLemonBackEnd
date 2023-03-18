from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(
            title="Pizza", price=150, inventory=50)
        self.menu2 = MenuItem.objects.create(
            title="Burger", price=80, inventory=30)
        self.menu3 = MenuItem.objects.create(
            title="Pasta", price=120, inventory=20)

    def test_get_all(self):
        response = self.client.get(reverse('menu-list'))
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
