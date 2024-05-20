from django.db import models
from userauths.models import User

class DashboardNotifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)


# Send an SMS to Vendor to provide his product for customer and send factor
class VendorNotificationSMS(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)