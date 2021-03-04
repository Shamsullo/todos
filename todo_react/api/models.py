from django.db import models
from datetime import datetime    

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_data = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title