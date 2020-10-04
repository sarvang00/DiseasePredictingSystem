from django.db import models
from django.conf import settings

from datetime import datetime

# Create your models here.
class HistoricalData(models.Model):
    case_of = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    case_reg_date = models.DateTimeField(default=datetime.now, blank=True)
    symptom_1 = models.CharField(max_length=50)
    symptom_2 = models.CharField(max_length=50)
    symptom_3 = models.CharField(max_length=50, blank=True)
    symptom_4 = models.CharField(max_length=50, blank=True)
    symptom_5 = models.CharField(max_length=50, blank=True)
    predicted_disease = models.CharField(max_length=50, blank=True)