from django.db import models

# Create your models here.

class HashTag(models.Model):

    name = models.CharField(max_length=30) # name VARCHAR(30) NOT NULL

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
