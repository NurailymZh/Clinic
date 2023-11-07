from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

class Receptionist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=6)

class DoctorType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, unique=True)

class DoctorStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, unique=True)

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_type_id = models.ForeignKey(DoctorType, on_delete=models.CASCADE)
    doctor_status_id = models.ForeignKey(DoctorStatus, on_delete=models.CASCADE)
    doctor_no = models.CharField(max_length=5, unique=True)
    doctor_count = models.CharField(max_length=5)
    price = models.CharField(max_length=10)

class PaymentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receptionist_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receptionist_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)

    