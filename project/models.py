from django.contrib.auth.models import AbstractUser
from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.name} ({self.date} at {self.time})'


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"Email: {self.email}, Name: {self.first_name}, Phone Number: {self.phone_number}, Breed: {self.breed}, " \
               f"Age: {self.age}, Password: {self.password}"


class ContactMessage(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
