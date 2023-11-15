from django.db import models
from django.utils import timezone

# Create your models here.
class GeneralFinancialData(models.Model):
    TITLE = models.CharField(max_length=255)
    TIME_PERIOD = models.DateField()
    OBS_VALUE = models.FloatField()

