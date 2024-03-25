from django.db import models
import datetime

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    desc = models.TextField(default='Default description')
    date = models.DateField(default=datetime.date.today)  


    def __str__(self):
        return self.name