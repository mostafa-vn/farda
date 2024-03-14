from django.db import models

# Create your models here.

import json

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):

    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    national_code = models.CharField(max_length=10, blank=True, null=True, unique=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    father_name = models.CharField(null=True, blank=True, max_length=100)
    extra = models.JSONField(null=True, blank=True)
    first_name = models.CharField(null=True, blank=True, max_length=200)
    last_name = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    skills = models.CharField(null=True, blank=True, max_length=50)  # create skills table
    network = models.CharField(null=True, blank=True, max_length=50)  # create network table
