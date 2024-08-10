from django.db import models
from app.helpers import model_conf
# Create your models here.


class Student(models.Model):
    name = models.CharField(**model_conf)
    std = models.CharField(**model_conf)
    result = models.CharField(**model_conf)
    
    
    