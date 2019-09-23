
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=40)
    register_date = models.DateTimeField(default=datetime.now, blank=True)


class Horse(models.Model):
     owner = models.ForeignKey(User, on_delete=models.CASCADE)
     breed = models.Charfield(max_length=40)
     skill = models.IntegerField(default = 0)
     date_of_birth = models.DateTimeField(default=datetime.now, blank=True)