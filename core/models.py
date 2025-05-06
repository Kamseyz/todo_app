from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()
# Create your models here.

class TODO(models.Model):
    title = models.CharField(max_length= 50, blank= True, null= False)
    content = models.TextField(max_length= 250, blank= True, null= False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title