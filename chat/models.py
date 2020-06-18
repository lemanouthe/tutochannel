from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

class salon(models.Model):
    """Model definition for salon."""
    nom = models.CharField(max_length=250)
    image = models.FileField(upload_to='Salon/')
    slug = AutoSlugField(populate_from='nom')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for salon."""

        verbose_name = 'salon'
        verbose_name_plural = 'salons'

    def __str__(self):
        """Unicode representation of salon."""
        return self.nom


class Message(models.Model):
    """Model definition for Message."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteur', null=True)
    salon = models.ForeignKey(salon, on_delete=models.CASCADE, related_name='salon_mesage', blank=True, null=True)
    message = models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Message."""
        unique_together = ['author', 'message']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
