from django.db import models
from userauths.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    date = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=20)
    brand = models.CharField(max_length=20, null=True, blank=True)
    part_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Part Number")
    quantity = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=20, null=True, blank=True)
    barcode = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='orders_image/', null=True, blank=True, verbose_name="Image") 
    dedicated_supplier_status = models.BooleanField(default=False, verbose_name="Dedicated Supplier Status")
    public_supplier_status = models.BooleanField(default=False, verbose_name="Public Supplier Status")
    related_group_status = models.BooleanField(default=False, verbose_name="Related Group Status")
    guarantee_status = models.BooleanField(default=False, verbose_name="Guarantee Status")

    def __str__(self):
        return f"{self.product} - {self.user}"