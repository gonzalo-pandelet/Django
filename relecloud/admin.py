from django.contrib import admin
from . import models

# Register your models here.

# mostrar las tablas en la pagina para el admin 
admin.site.register(models.Destination)
admin.site.register(models.Cruise)
admin.site.register(models.InfoRequest)

