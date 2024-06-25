from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from .models import Cliente, EstadoCliente, EstadoRegistro, TipoCliente,Personal, CargosPersonal,Actividad, EtapasProyecto, TiemposReales, PlantillaActividades
from .forms import ClienteForm,EstadoClienteForm,TipoClienteForm,PersonalForm, CargosPersonalForm,  ActividadForm, EtapasProyectoForm, TiemposRealesForm, PlantillaActividadesForm

def gestion_clientes(request):
    return render(request, 'gestion_clientes.html')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_add(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'cliente_list', 'title': 'Adicionar Cliente'})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'form.html', {'form': form, 'return_url': 'cliente_list', 'title': 'Modificar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        try:
            cliente.delete()
            return redirect('cliente_list')
        except IntegrityError:
            return render(request, 'cliente_confirm_delete.html', {'cliente': cliente, 'error': "No se puede eliminar el cliente porque tiene dependencias asociadas."})
    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})

def toggle_cliente_status(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    activo_estado = EstadoCliente.objects.get(EstCliNom='Activo')
    inactivo_estado = EstadoCliente.objects.get(EstCliNom='Inactivo')
    cliente.CliEst = inactivo_estado if cliente.CliEst == activo_estado else activo_estado
    cliente.save()
    return redirect('cliente_list')




# Estado Cliente CRUD
def estado_cliente_list(request):
    estados = EstadoCliente.objects.all()
    return render(request, 'estado_cliente_list.html', {'estados': estados})

def estado_cliente_add(request):
    if request.method == 'POST':
        form = EstadoClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_cliente_list')
    else:
        form = EstadoClienteForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'estado_cliente_list', 'title': 'Adicionar Estado Cliente'})

def estado_cliente_edit(request, pk):
    estado = get_object_or_404(EstadoCliente, pk=pk)
    if request.method == 'POST':
        form = EstadoClienteForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return redirect('estado_cliente_list')
    else:
        form = EstadoClienteForm(instance=estado)
    return render(request, 'form.html', {'form': form, 'return_url': 'estado_cliente_list', 'title': 'Modificar Estado Cliente'})

def estado_cliente_delete(request, pk):
    estado = get_object_or_404(EstadoCliente, pk=pk)
    if request.method == 'POST':
        estado.delete()
        return redirect('estado_cliente_list')
    return render(request, 'estado_cliente_confirm_delete.html', {'estado': estado})


# Tipo Cliente CRUD
def tipo_cliente_list(request):
    tipos = TipoCliente.objects.all()
    return render(request, 'tipo_cliente_list.html', {'tipos': tipos})

def tipo_cliente_add(request):
    if request.method == 'POST':
        form = TipoClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_cliente_list')
    else:
        form = TipoClienteForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'tipo_cliente_list', 'title': 'Adicionar Tipo Cliente'})

def tipo_cliente_edit(request, pk):
    tipo = get_object_or_404(TipoCliente, pk=pk)
    if request.method == 'POST':
        form = TipoClienteForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipo_cliente_list')
    else:
        form = TipoClienteForm(instance=tipo)
    return render(request, 'form.html', {'form': form, 'return_url': 'tipo_cliente_list', 'title': 'Modificar Tipo Cliente'})

def tipo_cliente_delete(request, pk):
    tipo = get_object_or_404(TipoCliente, pk=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('tipo_cliente_list')
    return render(request, 'tipo_cliente_confirm_delete.html', {'tipo': tipo})



def gestion_personal(request):
    return render(request, 'gestion_personal.html')

# Personal CRUD
def personal_list(request):
    personal = Personal.objects.all()
    return render(request, 'personal_list.html', {'personal': personal})

def personal_add(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'personal_list', 'title': 'Adicionar Personal'})

def personal_edit(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'form.html', {'form': form, 'return_url': 'personal_list', 'title': 'Modificar Personal'})

def personal_delete(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        personal.delete()
        return redirect('personal_list')
    return render(request, 'personal_confirm_delete.html', {'personal': personal})



# CargosPersonal CRUD
def cargo_personal_list(request):
    cargos = CargosPersonal.objects.all()
    return render(request, 'cargo_personal_list.html', {'cargos': cargos})

def cargo_personal_add(request):
    if request.method == 'POST':
        form = CargosPersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_personal_list')
    else:
        form = CargosPersonalForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'cargo_personal_list', 'title': 'Adicionar Cargo Personal'})

def cargo_personal_edit(request, pk):
    cargo = get_object_or_404(CargosPersonal, pk=pk)
    if request.method == 'POST':
        form = CargosPersonalForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo_personal_list')
    else:
        form = CargosPersonalForm(instance=cargo)
    return render(request, 'form.html', {'form': form, 'return_url': 'cargo_personal_list', 'title': 'Modificar Cargo Personal'})

def cargo_personal_delete(request, pk):
    cargo = get_object_or_404(CargosPersonal, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_personal_list')
    return render(request, 'cargo_personal_confirm_delete.html', {'cargo': cargo})
def gestion_actividades(request):
    return render(request, 'gestion_actividades.html')



# Actividad CRUD
def actividad_list(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividad_list.html', {'actividades': actividades})

def actividad_add(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'actividad_list', 'title': 'Adicionar Actividad'})

def actividad_edit(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'form.html', {'form': form, 'return_url': 'actividad_list', 'title': 'Modificar Actividad'})

def actividad_delete(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        actividad.delete()
        return redirect('actividad_list')
    return render(request, 'actividad_confirm_delete.html', {'actividad': actividad})



# Etapas Proyecto CRUD
def etapas_proyecto_list(request):
    etapas = EtapasProyecto.objects.all()
    return render(request, 'etapas_proyecto_list.html', {'etapas': etapas})

def etapas_proyecto_add(request):
    if request.method == 'POST':
        form = EtapasProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etapas_proyecto_list')
    else:
        form = EtapasProyectoForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'etapas_proyecto_list', 'title': 'Adicionar Etapa Proyecto'})

def etapas_proyecto_edit(request, pk):
    etapa = get_object_or_404(EtapasProyecto, pk=pk)
    if request.method == 'POST':
        form = EtapasProyectoForm(request.POST, instance=etapa)
        if form.is_valid():
            form.save()
            return redirect('etapas_proyecto_list')
    else:
        form = EtapasProyectoForm(instance=etapa)
    return render(request, 'form.html', {'form': form, 'return_url': 'etapas_proyecto_list', 'title': 'Modificar Etapa Proyecto'})

def etapas_proyecto_delete(request, pk):
    etapa = get_object_or_404(EtapasProyecto, pk=pk)
    if request.method == 'POST':
        etapa.delete()
        return redirect('etapas_proyecto_list')
    return render(request, 'etapas_proyecto_confirm_delete.html', {'etapa': etapa})


# Tiempos Reales CRUD
def tiempos_reales_list(request):
    tiempos = TiemposReales.objects.all()
    return render(request, 'tiempos_reales_list.html', {'tiempos': tiempos})

def tiempos_reales_add(request):
    if request.method == 'POST':
        form = TiemposRealesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tiempos_reales_list')
    else:
        form = TiemposRealesForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'tiempos_reales_list', 'title': 'Adicionar Tiempo Real'})

def tiempos_reales_edit(request, pk):
    tiempo = get_object_or_404(TiemposReales, pk=pk)
    if request.method == 'POST':
        form = TiemposRealesForm(request.POST, instance=tiempo)
        if form.is_valid():
            form.save()
            return redirect('tiempos_reales_list')
    else:
        form = TiemposRealesForm(instance=tiempo)
    return render(request, 'form.html', {'form': form, 'return_url': 'tiempos_reales_list', 'title': 'Modificar Tiempo Real'})

def tiempos_reales_delete(request, pk):
    tiempo = get_object_or_404(TiemposReales, pk=pk)
    if request.method == 'POST':
        tiempo.delete()
        return redirect('tiempos_reales_list')
    return render(request, 'tiempos_reales_confirm_delete.html', {'tiempo': tiempo})


# Plantilla Actividades CRUD
def plantilla_actividades_list(request):
    plantillas = PlantillaActividades.objects.all()
    return render(request, 'plantilla_actividades_list.html', {'plantillas': plantillas})

def plantilla_actividades_add(request):
    if request.method == 'POST':
        form = PlantillaActividadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plantilla_actividades_list')
    else:
        form = PlantillaActividadesForm()
    return render(request, 'form.html', {'form': form, 'return_url': 'plantilla_actividades_list', 'title': 'Adicionar Plantilla Actividades'})

def plantilla_actividades_edit(request, pk):
    plantilla = get_object_or_404(PlantillaActividades, pk=pk)
    if request.method == 'POST':
        form = PlantillaActividadesForm(request.POST, instance=plantilla)
        if form.is_valid():
            form.save()
            return redirect('plantilla_actividades_list')
    else:
        form = PlantillaActividadesForm(instance=plantilla)
    return render(request, 'form.html', {'form': form, 'return_url': 'plantilla_actividades_list', 'title': 'Modificar Plantilla Actividades'})

def plantilla_actividades_delete(request, pk):
    plantilla = get_object_or_404(PlantillaActividades, pk=pk)
    if request.method == 'POST':
        plantilla.delete()
        return redirect('plantilla_actividades_list')
    return render(request, 'plantilla_actividades_confirm_delete.html', {'plantilla': plantilla})

def toggle_personal_status(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    activo_estado = EstadoCliente.objects.get(EstCliNom='Activo')
    inactivo_estado = EstadoCliente.objects.get(EstCliNom='Inactivo')
    personal.PerEst = inactivo_estado if personal.PerEst == activo_estado else activo_estado
    personal.save()
    return redirect('personal_list')

def toggle_cargo_personal_status(request, pk):
    cargo = get_object_or_404(CargosPersonal, pk=pk)
    activo_estado = EstadoRegistro.objects.get(EstRegNom='Activo')
    inactivo_estado = EstadoRegistro.objects.get(EstRegNom='Inactivo')
    cargo.CarPerEstReg = inactivo_estado if cargo.CarPerEstReg == activo_estado else activo_estado
    cargo.save()
    return redirect('cargo_personal_list')

def toggle_actividad_status(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    activo_estado = EstadoRegistro.objects.get(EstRegNom='Activo')
    inactivo_estado = EstadoRegistro.objects.get(EstRegNom='Inactivo')
    actividad.ActEstReg = inactivo_estado if actividad.ActEstReg == activo_estado else activo_estado
    actividad.save()
    return redirect('actividad_list')

def toggle_etapa_proyecto_status(request, pk):
    etapa = get_object_or_404(EtapasProyecto, pk=pk)
    activo_estado = EstadoRegistro.objects.get(EstRegNom='Activo')
    inactivo_estado = EstadoRegistro.objects.get(EstRegNom='Inactivo')
    etapa.EtaProEstReg = inactivo_estado if etapa.EtaProEstReg == activo_estado else activo_estado
    etapa.save()
    return redirect('etapas_proyecto_list')
def toggle_tiempos_reales_status(request, pk):
    tiempo = get_object_or_404(TiemposReales, pk=pk)
    activo_estado = EstadoRegistro.objects.get(EstRegNom='Activo')
    inactivo_estado = EstadoRegistro.objects.get(EstRegNom='Inactivo')
    tiempo.TieReaEstReg = inactivo_estado if tiempo.TieReaEstReg == activo_estado else activo_estado
    tiempo.save()
    return redirect('tiempos_reales_list')

def toggle_plantilla_actividades_status(request, pk):
    plantilla = get_object_or_404(PlantillaActividades, pk=pk)
    activo_estado = EstadoRegistro.objects.get(EstRegNom='Activo')
    inactivo_estado = EstadoRegistro.objects.get(EstRegNom='Inactivo')
    plantilla.PlaActEstReg = inactivo_estado if plantilla.PlaActEstReg == activo_estado else activo_estado
    plantilla.save()
    return redirect('plantilla_actividades_list')



