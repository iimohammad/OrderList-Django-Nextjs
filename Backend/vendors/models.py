from django.db import models
from userauths.models import User
from orders.models import Order
from company.models import Company
from products.models import Product
from django.core.exceptions import ValidationError

# This model have to automatically fill
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.user is None and self.company is None:
            raise ValidationError("Either user or company must be set.")
        super().save(*args, **kwargs)

class ResponseOrders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    response_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    deliver_time = models.DateTimeField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    factor = models.FileField(upload_to='factor/')

    def __str__(self):
        return f"{self.order.name} response"
    
    class Meta:
        verbose_name = 'ResponseOrder'
        verbose_name_plural = "ResponseOrders"


# This model use to match vendors to orders 
