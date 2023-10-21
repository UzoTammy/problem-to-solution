from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone
from users.models import CustomUser as User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    review = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = MoneyField(max_digits=5, decimal_places=2, default_currency='CAD') 
    is_available = models.BooleanField(default=False)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

