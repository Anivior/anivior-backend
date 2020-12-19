from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email can't be null")
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self.create_user(email, password, **kwargs)


class NGO(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default=None)
    city = models.CharField(max_length=255, default='')
    pincode = models.PositiveIntegerField(default=0)
    contact = models.BigIntegerField(default=0)
    point = models.PointField(geography=True, default=Point(0.0, 0.0))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'






