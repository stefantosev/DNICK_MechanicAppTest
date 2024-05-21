from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=25)
    link = models.URLField()
    country = models.CharField(max_length=25)
    owner = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} ({self.link})"


class Workshop(models.Model):
    name = models.CharField(max_length=25)
    yearEstablished = models.DateTimeField()
    oldTimerFixes = models.BooleanField(default=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Automobiles(models.Model):
    type = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    allowedSpeed = models.IntegerField()
    color = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.type} - {self.color}"


class ScheduledRepair(models.Model):
    code = models.CharField(max_length=25)
    date = models.DateField()
    description = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    carInfo = models.ForeignKey(Automobiles, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.date}"