from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def compradores(request):
    contexto = {"compradores": Comprador.objects.all()}
    return render(request, "aplicacion/compradores.html", contexto)

def vendedores(request):
    contexto = {"vendedores": Vendedor.objects.all()}
    return render(request, "aplicacion/vendedores.html",contexto)

def productos(request):
    contexto = {"productos": Producto.objects.all()}
    return render(request, "aplicacion/productos.html",contexto)

def acerca(request):
    return render(request, "aplicacion/acerca.html")

def mas_info_contacto(request):
    return render(request, "aplicacion/mas_info_contacto.html")

#__________________________Formularios

def compradorForm(request):
    if request.method == "POST":
        miForm = CompradorForm(request.POST)
        if miForm.is_valid():
            comprador_nombre = miForm.cleaned_data.get("nombre")
            comprador_domicilio = miForm.cleaned_data.get("domicilio")
            comprador_nro_documento = miForm.cleaned_data.get("nro_documento")
            comprador = Comprador(nombre=comprador_nombre,domicilio=comprador_domicilio,nro_documento=comprador_nro_documento)
            comprador.save()
            contexto = {"compradores": Comprador.objects.all()}
            return render(request, "aplicacion/compradores.html", contexto)
    else:
        miForm = CompradorForm()
    
    return render(request,'aplicacion/compradorForm.html', {"form": miForm})


def vendedorForm(request):
    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        if miForm.is_valid():
            vendedor_nombre = miForm.cleaned_data.get("nombre")
            vendedor_nro_documento = miForm.cleaned_data.get("nro_documento")
            vendedor = Vendedor(nombre=vendedor_nombre,nro_documento=vendedor_nro_documento)
            vendedor.save()
            contexto = {"vendedores": Vendedor.objects.all()}
            return render(request, "aplicacion/vendedores.html", contexto)
    else:
        miForm = VendedorForm()
    
    return render(request,'aplicacion/vendedorForm.html', {"form": miForm})


def productoForm(request):
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_nro_item = miForm.cleaned_data.get("nro_item")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Producto(nombre=producto_nombre,nro_item=producto_nro_item,precio=producto_precio)
            producto.save()
            contexto = {"productos": Producto.objects.all()}
            return render(request, "aplicacion/productos.html")
    else:
        miForm = ProductoForm()
    
    return render(request,'aplicacion/productoForm.html', {"form": miForm})



#____________________________Buscador

def buscar_productos(request):
    return render(request, "aplicacion/buscar.html")

def encontrar_productos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains = patron)
        contexto = {'productos': productos}
    else:
        contexto = {'productos': Producto.objects.all()}
    
    return render(request, 'aplicacion/productos.html', contexto)