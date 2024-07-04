from django import forms

class CompradorForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Apellido y Nombre")
    domicilio = forms.CharField(max_length=30,required=True,label="Domicilio")
    nro_documento = forms.IntegerField(required=True,label="Número de Documento")

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Apellido y Nombre")
    nro_documento = forms.IntegerField(required=True,label="Número de Documento")

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Nombre de Producto")
    nro_item = forms.IntegerField(required=True,label="Número de Ítem")
    precio = forms.DecimalField(max_digits=10, decimal_places=3, required=True,label="Precio")

