from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from django.utils import timezone

def inicio_ventas(request):
    # Página principal con info simple
    return render(request, 'inicio.html', {})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        empresa = request.POST.get('empresa', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        email = request.POST.get('email', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        ciudad = request.POST.get('ciudad', '').strip()

        Proveedor.objects.create(
            nombre=nombre,
            empresa=empresa,
            telefono=telefono,
            email=email,
            direccion=direccion,
            ciudad=ciudad,
        )
        return redirect('app_Venta_Telefonos:ver_proveedores')

    return render(request, 'proveedor/agregar_proveedor.html', {})

def ver_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('-fecha_registro')
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    # recibe POST con campos actualizados
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre', proveedor.nombre)
        proveedor.empresa = request.POST.get('empresa', proveedor.empresa)
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono)
        proveedor.email = request.POST.get('email', proveedor.email)
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion)
        proveedor.ciudad = request.POST.get('ciudad', proveedor.ciudad)
        proveedor.save()
        return redirect('app_Venta_Telefonos:ver_proveedores')

    # si no es POST, redirige a ver
    return redirect('app_Venta_Telefonos:ver_proveedores')

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('app_Venta_Telefonos:ver_proveedores')
    # GET -> mostrar confirmación
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})
