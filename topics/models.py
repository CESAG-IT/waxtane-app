from django.db import models
from tags.models import HashTag

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    image_topic = models.ImageField(upload_to="topics/", default="default.png")
    is_deleted = models.BooleanField(default=False)
    tag_id  = models.ForeignKey(HashTag, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
