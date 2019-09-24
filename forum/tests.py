from django.urls import reverse
from django.urls import resolve
from django.test import TestCase

from .views import *
from .models import Board

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
