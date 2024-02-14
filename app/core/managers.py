"""
User Managers
"""

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ manager for users .  """

    def create_user(self, email, password=None, **extra_fields):
        """ create , save and return a new user """
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
