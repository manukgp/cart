from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class ShoppingItem(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    description = models.TextField(max_length=220, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(default='default.jpg', upload_to='item_images/')

    def discounted_price(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return self.item
    

