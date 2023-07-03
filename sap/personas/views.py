from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


# Create your views here.

def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


# PersonaForm = modelform_factory(Persona, exclude=[])


def agregarPersona(request):
    if request.method == 'POST':
        formPersona = PersonaForm(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('index')

    else:
        formPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formPersona': formPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formPersona = PersonaForm(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('index')

    else:
        formPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formPersona': formPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
        return redirect('index')


def listadoDirecciones(request):
    numero_direcciones = Domicilio.objects.count()
    direcciones = Domicilio.objects.order_by('id', 'calle')
    return render(request, 'direcciones/listado.html',
                  {'no_direcciones': numero_direcciones, 'direcciones': direcciones})


def agregarDireccion(request):
    if request.method == 'POST':
        formDireccion = DomicilioForm(request.POST)
        if formDireccion.is_valid():
            formDireccion.save()
            return redirect('index')

    else:
        formDireccion = DomicilioForm()

    return render(request, 'direcciones/nuevo.html', {'formDireccion': formDireccion})


def editarDireccion(request, id):
    direccion = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formDireccion = DomicilioForm(request.POST, instance=direccion)
        if formDireccion.is_valid():
            formDireccion.save()
            return redirect('index')

    else:
        formDireccion = DomicilioForm(instance=direccion)

    return render(request, 'direcciones/editar.html', {'formDireccion': formDireccion})


def detalleDireccion(request, id):
    direccion = get_object_or_404(Domicilio, pk=id)
    return render(request, 'direcciones/detalle.html', {'domicilio': direccion})
