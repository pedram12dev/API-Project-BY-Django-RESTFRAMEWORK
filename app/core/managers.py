"""
User Managers
"""

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ manager for users .  """

    def create_user(self, email, password=None, **extra_fields):
        """ create , save and return a new user """
        if not email:
            raise ValueError(' Users must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
