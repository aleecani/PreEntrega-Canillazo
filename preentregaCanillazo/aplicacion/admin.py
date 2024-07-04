from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Comprador)
admin.site.register(Vendedor)
admin.site.register(Producto)