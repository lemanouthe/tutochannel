from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    """Model definition for Message."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteur', blank=True, null=True)
    message = models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Message."""
        unique_together = [['author', 'message']]
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
