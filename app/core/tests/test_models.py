"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):
    """test models"""

    def test_create_user_with_email_successful(self):
        """ test create a user with an email successful"""
        email = 'email@example.com'
        password = 'root'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
