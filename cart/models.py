from django.conf import settings
from django.db import models
from products.models import Product
class Cart(models.Model):
user=usermodels.OneToOneField(settings .AUTH_USER_MODEL, on_delete=models. CASCADE, related_name='cart')
class CartItem(models.Model):
 cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items')
 product = models.ForeignKey(Product, on_delete=models.CASCADE)quantity = models.PositiveIntegerField(default=1)
  classMeta:classconstraints[models.UniqueConstraint(fields=['cart','product'], name='unique_cart_product')]
