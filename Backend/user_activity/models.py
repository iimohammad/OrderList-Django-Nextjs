from django.db import models
from userauths.models import User
from products.models import Brand, Tag, Category
from company.models import Company

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_field = models.CharField(max_length=50,null=True, blank=True)
    brands_related = models.ForeignKey(Brand,on_delete=models.CASCADE)
    tags_related = models.ForeignKey(Tag,on_delete=models.CASCADE)
    categoried_related = models.ForeignKey(Category,on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.company and not Company.objects.filter(name=self.company).exists():
            Company.objects.create(name=self.company)
        super().save(*args, **kwargs)