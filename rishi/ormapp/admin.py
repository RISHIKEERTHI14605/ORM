from django.contrib import admin
from .models import Railway, RailwayAdmin

admin.site.register(Railway, RailwayAdmin)