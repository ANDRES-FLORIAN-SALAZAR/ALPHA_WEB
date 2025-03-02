from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the home page")