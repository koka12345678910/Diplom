from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    email = models.EmailField(unique=True)
    telegram_id = models.CharField(max_length=64, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class OTPRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.code}"

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)
