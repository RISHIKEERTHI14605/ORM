from django.db import models
from django.contrib import admin

class Railway(models.Model):    
    Train_no = models.IntegerField(primary_key=True)
    Train_name = models.CharField(max_length=50)
    Start_station_code = models.CharField(max_length=20)
    End_station_code = models.CharField(max_length=20)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField() 
 
class RailwayAdmin(admin.ModelAdmin):
    list_display = ('Train_no','Train_name','Start_station_code','End_station_code','Start_date','End_date')
