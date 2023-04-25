from django.test import TestCase

# Create your tests here.


from django.urls import reverse

from django.contrib.auth.models import User


class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.url = reverse('login')
        self.credentials = {'username': 'testuser', 'password': 'testpass'}

    # Test that submitting the login form with valid credentials redirects to the home page:
    def test_login_valid(self):
        response = self.client.post(self.url, self.credentials, follow=True)
        self.assertRedirects(response, reverse('home'))

    # Test that submitting the login form with invalid credentials shows the correct error message:
    def test_login_invalid(self):
        response = self.client.post(self.url, self.bad_credentials, follow=True)
        self.assertContains(response, 'Please enter a correct username and password.')


from django.contrib.auth.models import User


class SignupTests(TestCase):
    def setUp(self):
        self.url = reverse('signup')
        self.credentials = {'username': 'testuser', 'password1': 'testpass', 'password2': 'testpass'}

    # Test that the sign up page loads correctly:
    def test_signup_page_loads_correctly(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')


self.assertTemplateUsed(response, 'registration/signup.html')