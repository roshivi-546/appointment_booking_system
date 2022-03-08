from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class profession(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class state(models.Model):
    profession = models.ForeignKey(profession, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class dist(models.Model):
    profession = models.ForeignKey(profession, on_delete = models.CASCADE)
    state = models.ForeignKey(state, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=13)
    image = models.ImageField(null = True, blank = True)
    password = models.CharField(max_length=100)
    profession = models.ForeignKey(profession, on_delete = models.DO_NOTHING, null=True, default=1)
    state_name = models.ForeignKey(state, on_delete = models.DO_NOTHING, null=True, default=1)
    dist_name = models.ForeignKey(dist, on_delete = models.DO_NOTHING, null=True, default=1)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank = False, null = True)
    reason = models.CharField(max_length=500)
    remark = models.CharField(max_length=500, default = True)
    date_and_time = models.DateTimeField(auto_now_add=False, null=True)
    date_time = models.DateTimeField(auto_now_add=True, blank= True, null=False)
    accepted = models.BooleanField(default = False)
    accepted_date = models.DateTimeField(blank=True, null=True)
    specialist = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING, null=True, default=1)
    profession = models.ForeignKey(profession, on_delete = models.DO_NOTHING, null=True, default=1)
    state_name = models.ForeignKey(state, on_delete = models.DO_NOTHING, null=True, default=1)
    dist_name = models.ForeignKey(dist, on_delete = models.DO_NOTHING, null=True, default=1)

    
