from django.test import TestCase

# Create your tests here.
"""
from django.urls import reverse

from django.contrib.auth.models import User


class LoginTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.url = reverse('login')
        self.bad_credentials = {'username': 'testuser', 'password': 'wrongpass'}

    def test_login_invalid(self):
        response = self.client.post(self.url, self.bad_credentials, follow=True)
        self.assertContains(response, 'Please enter a correct username and password.')


# Test that submitting the login form with valid credentials redirects to the home page:
class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.url = reverse('login')
        self.credentials = {'username': 'testuser', 'password': 'testpass'}

    def test_login_valid(self):
        response = self.client.post(self.url, self.credentials, follow=True)
        self.assertRedirects(response, reverse('home'))
"""
# Test that sumbitting the login form with valid credentials redirects to the home page:
from django.urls import reverse

from django.contrib.auth.models import User


class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.url = reverse('login')
        self.credentials = {'username': 'testuser', 'password': 'testpass'}

    def test_login_valid(self):
        response = self.client.post(self.url, self.credentials, follow=True)
        self.assertRedirects(response, reverse('home'))

# Test that submitting the login form with invalid credentials shows the correct error message:
#from django.urls import reverse

#from django.contrib.auth.models import User



class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.url = reverse('login')
        self.bad_credentials = {'username': 'testuser', 'password': 'wrongpass'}

    def test_login_invalid(self):
        response = self.client.post(self.url, self.bad_credentials, follow=True)
        self.assertContains(response, 'Please enter a correct username and password.')

# Test that the sign up page loads correctly:
#from django.urls import reverse

from django.contrib.auth.models import User


class SignupTests(TestCase):
    def setUp(self):
        self.url = reverse('signup')
        self.credentials = {'username': 'testuser', 'password1': 'testpass', 'password2': 'testpass'}

    def test_signup_page_loads_correctly(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')