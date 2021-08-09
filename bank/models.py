from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=25)
    current_balance = models.FloatField(validators=[MinValueValidator(3000.00)])

class Transfer(models.Model):
    transfer_from = models.ForeignKey(Customers, related_name="transfer_from", on_delete=models.CASCADE, null=True)
    transfer_to = models.ForeignKey(Customers, related_name="transfer_to", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(validators=[MaxValueValidator(100000.00)])
