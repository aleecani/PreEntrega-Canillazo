from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('compradores/', compradores, name="compradores"),
    path('vendedores/', vendedores, name="vendedores"),
    path('productos/', productos, name="productos"),
    
    path('acerca/', acerca, name="acerca"),
    path('mas_info_contacto/', mas_info_contacto, name="mas_info_contacto"),
    
    #Formularios_____
    path('compradorForm/', compradorForm, name="compradorForm"),
    path('vendedorForm/', vendedorForm, name="vendedorForm"),
    path('productoForm/', productoForm, name="productoForm"),
        
    #Buscar_______
    path('buscar_productos/', buscar_productos , name="buscar_productos"),
    path('encontrar_productos/', encontrar_productos , name="encontrar_productos"),

]