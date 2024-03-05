from django.db import models

class Order(models.Model):
    academic_level = models.CharField(max_length=200)
    service_type = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)