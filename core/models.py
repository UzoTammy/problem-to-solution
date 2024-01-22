from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone
from users.models import CustomUser as User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    alias = models.CharField(max_length=4)
    category = models.CharField(max_length=50)
    short_message = models.CharField(max_length=200, default="")
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

