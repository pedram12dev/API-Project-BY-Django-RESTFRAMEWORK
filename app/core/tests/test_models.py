"""
Test for models.
"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


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

    def test_new_user_email_normalized(self):
        """Test email normalized for new user"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'root')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'root1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'root123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe successful"""
        user = get_user_model().objects.create_user(
            'test5@email.com',
            'testpass1234',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='recipe title ',
            time_minutes=5,
            price=Decimal(5.50),
            description=' sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
