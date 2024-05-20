from django.db import models
from orders.models import Order
from userauths.models import User

class orderRequestCost(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order ID: {self.order.id}, Price: {self.price}"
    

class membershipCost(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    membership_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)