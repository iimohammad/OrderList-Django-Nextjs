from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    description = models.TextField()

    class Meta:
        verbose_name = 'Category'  
        verbose_name_plural = 'Categories'  

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name.startswith("#"):
            self.name = "#" + self.name
        super().save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=20)
    partnumber = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')
    catalog = models.FileField(upload_to='product_catalog/',null=True,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        )
    
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name
    

    class Meta:
        unique_together = ('name', 'partnumber', 'brand')