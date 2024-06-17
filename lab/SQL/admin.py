from django.contrib import admin

from .models import EstadoRegistro, EstadoCliente, TipoCliente, Cliente, TipoProyecto, EstadoProyecto, Proyecto, DuracionProyecto, EtapasProyecto, CargosPersonal, Personal, CargosProyecto, PersonalCargosProyecto, ProyectoPersonalCargosProyecto, ProyectoMovimientos, PlantillaActividades, Actividad, TiemposReales

admin.site.register(EstadoRegistro)
admin.site.register(EstadoCliente)
admin.site.register(TipoCliente)
admin.site.register(Cliente)
admin.site.register(TipoProyecto)
admin.site.register(EstadoProyecto)
admin.site.register(Proyecto)
admin.site.register(DuracionProyecto)
admin.site.register(EtapasProyecto)
admin.site.register(CargosPersonal)
admin.site.register(Personal)
admin.site.register(CargosProyecto)
admin.site.register(PersonalCargosProyecto)
admin.site.register(ProyectoPersonalCargosProyecto)
admin.site.register(ProyectoMovimientos)
admin.site.register(PlantillaActividades)
admin.site.register(Actividad)
admin.site.register(TiemposReales)
