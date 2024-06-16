from django.db import models

# Create your models here.

class BusinessEmploymentData(models.Model):
    series_reference=models.CharField(max_length=200)
    Period=models.FloatField()
    Data_value=models.CharField(max_length=100)
    Suppressed=models.CharField(max_length=100,null=True)
    STATUS=models.CharField(max_length=100)
    UNITS=models.CharField(max_length=100)
    Magnitude=models.IntegerField()
    Subject=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=100)
    Series_title_2=models.CharField(max_length=300)
    Series_title_3=models.CharField(max_length=100)
    Series_title_4=models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.series_reference