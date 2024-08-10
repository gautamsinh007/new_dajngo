from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(**model_conf)
    std = models.CharField(**model_conf)
    result = models.CharField(**model_conf)
    