from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch

from core import models


class ModelTests(TestCase):

    def __sample_user(email='test@gmail.com', password='testpass123'):
        """Create a sample user"""
        return get_user_model().objects.create_user(email, password)

    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = '12345678'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
    	"""Test the email for a new user is normalized"""
    	email = 'test@GMAIL.COM'
    	user = get_user_model().objects.create_user(email, 'test123')

    	self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_creata_new_superuser(self):
        """ Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
