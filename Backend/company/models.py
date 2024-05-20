from django.db import models
from products.models import Brand, Tag, Category

class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.TextField(null=True, blank=True)
    phone_Number = models.CharField(max_length=15,null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = "Companies"


class CompanyActvity(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    work_field = models.CharField(max_length=50,null=True, blank=True)
    brands_related = models.ForeignKey(Brand,on_delete=models.CASCADE)
    tags_related = models.ForeignKey(Tag,on_delete=models.CASCADE)
    categoried_related = models.ForeignKey(Category,on_delete=models.CASCADE)