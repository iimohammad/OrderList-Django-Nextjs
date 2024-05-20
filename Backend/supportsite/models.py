from django.db import models
from userauths.models import User

class MessageForSupport(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=50)
    message = models.TextField()
    attachment = models.FileField(upload_to='support/', blank=True, null=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"
