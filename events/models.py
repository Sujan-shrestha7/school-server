from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False),
    description = models.TextField(blank=False, null=False),
    image = models.ImageField(upload_to='event_images'),