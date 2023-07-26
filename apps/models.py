from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    position = models.CharField(max_length=200, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'user'


class Service(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


class Portfolio(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    cotegory = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


class Price(models.Model):
    basic = models.CharField(max_length=200, null=True, blank=True)
    premium = models.CharField(max_length=200, null=True, blank=True)


class Blog(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
