from django.http import HttpResponse
from django.shortcuts import redirect, render

from inventario.forms import ProductosForm
from inventario.models import productos


def tests(request):
    return render(request, 'tests.html')
def menu(request):
    return render(request, 'menu.html')


def inventario(request):
    productoss = productos.objects.all()
    context = {'productos': productoss}
    return render(request, 'inventario.html', context)


def agregar_producto(request):
    if request.method == "POST":
        form = ProductosForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/tests")
            except:
                pass
    else:
        form = ProductosForm()
    return render(request, "tests.html", {'form': form})


def editar_producto(request, id):
    productoss = productos.objects.get(clave_producto=id)

    return render(request, 'editar_producto.html', {'productos': productoss})


def eliminar_producto(request, id):
    productoss = productos.objects.get(clave_producto=id)
    productoss.delete()
    return redirect('/inventario')


def ventas(request):
    return render(request, 'ventas.html')


def compras(request):
    return render(request, 'compras.html')
