from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    

    def __str__(self):
        return self.content
    