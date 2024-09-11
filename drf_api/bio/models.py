from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class Bio(models.Model):
    """
    This will create the bio or profile of each user created, shall add the image part later on.
    """
    owner =models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, default='')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    content =models.TextField(default=True)

    def __str__(self):
        return f"{self.owner}"
    
    class Meta:
        ordering = ['-created_at']

