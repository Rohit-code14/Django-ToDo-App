from django.db import models
import datetime

# Create your models here.
class task(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
    
