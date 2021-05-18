
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, number, password, **extra_fields):
        """Create and save a User with the given number and password."""
        if not number:
            raise ValueError('The given number must be set')
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, number, password=None, **extra_fields):
        """Create and save a regular User with the given number and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(number, password, **extra_fields)

    def create_superuser(self, number, password, **extra_fields):
        """Create and save a SuperUser with the given number and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(number, password, **extra_fields)


class User(AbstractUser):
    username = None
    number = models.CharField( max_length=15, unique=True)
    my_ref = models.CharField(max_length=6, unique=True, default=0000)
    inv_ref = models.CharField(max_length=6, blank=True, default=None, null=True)
    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        # protect current referal from rewriting
        super().save(*args, **kwargs)





