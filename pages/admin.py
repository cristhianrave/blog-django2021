from django.contrib import admin
from pages.models import Page
# Register your models here.

admin.site.register(Page) # Clase de la bbdd  


# Configuracion del panel admin
title = "Panel admin"
subtitle = "Project Django"    

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle