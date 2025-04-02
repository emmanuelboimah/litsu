from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
    )
    user_type = models.CharField(choices=USER, max_length=58, default=1)
    