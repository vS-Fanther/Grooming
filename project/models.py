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


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField

    def __str__(self):
        return f"Pet: {self.name}, Breed: {self.breed}"


class ContactMessage(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
