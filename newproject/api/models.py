from django.db import models

# Create your models here.
class User(models.Model):
    age=models.IntegerField()
    name=models.CharField(20)
    def __str__(self):
        return self.name
