from django.db import models
import uuid
from account import models as account_models

class Diagnose(models.Model):
    name = models.CharField(max_length=20, unique=True, default="")

class Service(models.Model):
    name = models.CharField(max_length=30, default="")
    img = models.ImageField(upload_to='services')
    price = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=250, default="")
    doctor = models.ForeignKey(account_models.CustomUser, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    patient = models.ForeignKey(account_models.CustomUser, related_name='patient_id', on_delete=models.CASCADE)
    doctor = models.ForeignKey(account_models.CustomUser, related_name='doctor_id', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order_time = models.DateTimeField()

class DayofWeek(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class WorkingTime(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class DoctorsSchedule(models.Model):
    doctor = models.ForeignKey(account_models.CustomUser, on_delete=models.CASCADE)
    day_of_week = models.ForeignKey(DayofWeek, on_delete=models.CASCADE)
    working_time = models.ForeignKey(WorkingTime, on_delete=models.CASCADE)
