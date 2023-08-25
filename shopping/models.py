from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class ShoppingItem(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField(max_length=220, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(default='default.jpg', upload_to='item_images/')

    def discounted_price(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return self.item
    
    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk':self.pk})