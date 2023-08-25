from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class PasswordsChangeViewTestCase(TestCase):
    def test_password_change_view(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')

        self.client.login(username='testuser', password='testpassword')

        form_data = {
            'old_password': 'testpassword',
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword',
        }

        response = self.client.post(reverse('password'), data=form_data)

        self.assertRedirects(response, reverse('profile'))

class RegisterViewTestCase(TestCase):
    def test_register_view(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newtestpassword',
            'password2': 'newtestpassword',
        }

        response = self.client.post(reverse('register'), data=form_data)

        self.assertRedirects(response, reverse('login'))

class ProfileViewTestCase(TestCase):
    def test_profile_view_authenticated_user(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('profile'))

        # Checking if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_unauthenticated_user(self):
        # Making a GET request to the profile view without logging in
        response = self.client.get(reverse('profile'))

        # Checking if the response status code is 302 (redirect to login)
        self.assertEqual(response.status_code, 302)
