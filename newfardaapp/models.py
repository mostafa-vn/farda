from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, blank=False, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True, max_length=200)
    last_name = models.CharField(blank=True, null=True, max_length=200)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)


    python = models.IntegerField(blank=True, null=True)
    bash = models.IntegerField(blank=True, null=True)
    linux = models.IntegerField(blank=True, null=True)


    network1 = models.CharField(blank=True, null=True, max_length=200)
    network2 = models.CharField(blank=True, null=True, max_length=200)
    network3 = models.CharField(blank=True, null=True, max_length=200)
    network4 = models.CharField(blank=True, null=True, max_length=200)
    network5 = models.CharField(blank=True, null=True, max_length=200)
    network6 = models.CharField(blank=True, null=True, max_length=200)
    network7 = models.CharField(blank=True, null=True, max_length=200)
    network8 = models.CharField(blank=True, null=True, max_length=200)
    network9 = models.CharField(blank=True, null=True, max_length=200)
    network10 = models.CharField(blank=True, null=True, max_length=200)


    def __str__(self):
        return self.user.first_name