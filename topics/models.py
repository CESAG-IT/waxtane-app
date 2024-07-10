from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    