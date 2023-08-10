from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class ShoppingItem(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField(max_length=220, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0)])

    def discounted_price(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return self.item


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True)


    def __str__(self):
        return self.first_name
    

