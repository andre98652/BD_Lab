import datetime
from django import forms
from .models import Cliente, EstadoCliente, TipoCliente,Personal, CargosPersonal, Actividad, EtapasProyecto, TiemposReales, PlantillaActividades


class ClienteForm(forms.ModelForm):
    CliFecIng = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    CliFecCes = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}), required=False)
    
    class Meta:
        model = Cliente
        fields = ['CliCod', 'CliNom', 'CliTip', 'CliFecIng', 'CliFecCes', 'CliEst', 'CliEstReg']
        widgets = {
            'CliCod': forms.TextInput(attrs={'class': 'form-control'}),
            'CliNom': forms.TextInput(attrs={'class': 'form-control'}),
            'CliTip': forms.Select(attrs={'class': 'form-control'}),
            'CliFecIng': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CliFecCes': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'CliEst': forms.Select(attrs={'class': 'form-control'}),
            'CliEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'CliCod': 'Código',
            'CliNom': 'Nombre',
            'CliTip': 'Tipo',
            'CliFecIng': 'Fecha de Ingreso',
            'CliFecCes': 'Fecha de Cese',
            'CliEst': 'Estado',
            'CliEstReg': 'Estado de Registro',
        }
        error_messages = {
            'CliCod': {
                'unique': "Ya existe un cliente con este código.",
                'required': "El código del cliente es obligatorio."
            },
            'CliNom': {
                'required': "El nombre del cliente es obligatorio."
            },
            'CliTip': {
                'required': "El tipo de cliente es obligatorio."
            },
            'CliEst': {
                'required': "El estado del cliente es obligatorio."
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['CliFecIng'].initial = datetime.date.today()
            self.fields['CliEst'].initial = EstadoCliente.objects.get(EstCliNom='Activo')
            self.fields['CliEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['CliCod'].widget.attrs['readonly'] = True

class EstadoClienteForm(forms.ModelForm):
    class Meta:
        model = EstadoCliente
        fields = ['EstCliCod', 'EstCliNom', 'EstCliEstReg']
        widgets = {
            'EstCliCod': forms.TextInput(attrs={'class': 'form-control'}),
            'EstCliNom': forms.TextInput(attrs={'class': 'form-control'}),
            'EstCliEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'EstCliCod': 'Código',
            'EstCliNom': 'Nombre',
            'EstCliEstReg': 'Estado de Registro',
        }
        error_messages = {
            'EstCliCod': {
                'unique': "Ya existe un estado con este código.",
                'required': "El código del estado es obligatorio."
            },
            'EstCliNom': {
                'required': "El nombre del estado es obligatorio."
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(EstadoClienteForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['EstCliEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['EstCliCod'].widget.attrs['readonly'] = True

class TipoClienteForm(forms.ModelForm):
    class Meta:
        model = TipoCliente
        fields = ['TipCliCod', 'TipCliNom', 'TipCliEstReg']
        widgets = {
            'TipCliCod': forms.TextInput(attrs={'class': 'form-control'}),
            'TipCliNom': forms.TextInput(attrs={'class': 'form-control'}),
            'TipCliEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'TipCliCod': 'Código',
            'TipCliNom': 'Nombre',
            'TipCliEstReg': 'Estado de Registro',
        }
        error_messages = {
            'TipCliCod': {
                'unique': "Ya existe un tipo de cliente con este código.",
                'required': "El código del tipo de cliente es obligatorio."
            },
            'TipCliNom': {
                'required': "El nombre del tipo de cliente es obligatorio."
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(TipoClienteForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['TipCliEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['TipCliCod'].widget.attrs['readonly'] = True

from django import forms
from django.utils import timezone
from .models import Personal, EstadoCliente, EstadoRegistro

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['PerCod', 'PerNom', 'PerCar', 'PerCosHor', 'PerFecIng', 'PerEst', 'PerEstReg']
        widgets = {
            'PerCod': forms.TextInput(attrs={'class': 'form-control'}),
            'PerNom': forms.TextInput(attrs={'class': 'form-control'}),
            'PerCar': forms.Select(attrs={'class': 'form-control'}),
            'PerCosHor': forms.NumberInput(attrs={'class': 'form-control'}),
            'PerFecIng': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'PerEst': forms.Select(attrs={'class': 'form-control'}),
            'PerEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'PerCod': 'Código',
            'PerNom': 'Nombre',
            'PerCar': 'Cargo',
            'PerCosHor': 'Costo por Hora',
            'PerFecIng': 'Fecha de Ingreso',
            'PerEst': 'Estado',
            'PerEstReg': 'Estado de Registro',
        }

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['PerCod'].widget.attrs['readonly'] = True
        else:
            self.fields['PerFecIng'].initial = timezone.now().date()
            self.fields['PerEst'].initial = EstadoCliente.objects.get(EstCliNom='Activo')
            self.fields['PerEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')


class CargosPersonalForm(forms.ModelForm):
    class Meta:
        model = CargosPersonal
        fields = ['CarPerCod', 'CarPerNom', 'CarPerEstReg']
        widgets = {
            'CarPerCod': forms.TextInput(attrs={'class': 'form-control'}),
            'CarPerNom': forms.TextInput(attrs={'class': 'form-control'}),
            'CarPerEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'CarPerCod': 'Código',
            'CarPerNom': 'Nombre',
            'CarPerEstReg': 'Estado de Registro',
        }
    def __init__(self, *args, **kwargs):
        super(CargosPersonalForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['CarPerEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['CarPerCod'].widget.attrs['readonly'] = True




class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['ActCod', 'ActNom', 'ActDes', 'ActTieEst', 'ActEstReg', 'ActCodPla', 'ActCodEta']
        widgets = {
            'ActCod': forms.TextInput(attrs={'class': 'form-control'}),
            'ActNom': forms.TextInput(attrs={'class': 'form-control'}),
            'ActDes': forms.Textarea(attrs={'class': 'form-control'}),
            'ActTieEst': forms.NumberInput(attrs={'class': 'form-control'}),
            'ActEstReg': forms.Select(attrs={'class': 'form-control'}),
            'ActCodPla': forms.Select(attrs={'class': 'form-control'}),
            'ActCodEta': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'ActCod': 'Código',
            'ActNom': 'Nombre',
            'ActDes': 'Descripción',
            'ActTieEst': 'Tiempo Estimado',
            'ActEstReg': 'Estado de Registro',
            'ActCodPla': 'Plantilla de Actividades',
            'ActCodEta': 'Etapa del Proyecto',
        }

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['ActEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['ActCod'].widget.attrs['readonly'] = True
            
class EtapasProyectoForm(forms.ModelForm):
    class Meta:
        model = EtapasProyecto
        fields = ['EtaProCod', 'EtaProNom', 'EtaProTieEst', 'EtaProEstReg']
        widgets = {
            'EtaProCod': forms.TextInput(attrs={'class': 'form-control'}),
            'EtaProNom': forms.TextInput(attrs={'class': 'form-control'}),
            'EtaProTieEst': forms.NumberInput(attrs={'class': 'form-control'}),
            'EtaProEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'EtaProCod': 'Código',
            'EtaProNom': 'Nombre',
            'EtaProTieEst': 'Tiempo Estimado',
            'EtaProEstReg': 'Estado de Registro',
        }

    def __init__(self, *args, **kwargs):
        super(EtapasProyectoForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['EtaProEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['EtaProCod'].widget.attrs['readonly'] = True


class TiemposRealesForm(forms.ModelForm):
    TieReaFecReg = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    
    class Meta:
        model = TiemposReales
        fields = ['TieReaCod', 'TieReaCodAct', 'TieReaAct', 'TieReaComAju', 'TieReaFecReg', 'TieReaEstReg']
        widgets = {
            'TieReaCod': forms.TextInput(attrs={'class': 'form-control'}),
            'TieReaCodAct': forms.Select(attrs={'class': 'form-control'}),
            'TieReaAct': forms.NumberInput(attrs={'class': 'form-control'}),
            'TieReaComAju': forms.Textarea(attrs={'class': 'form-control'}),
            'TieReaFecReg': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TieReaEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'TieReaCod': 'Código',
            'TieReaCodAct': 'Actividad',
            'TieReaAct': 'Tiempo Real',
            'TieReaComAju': 'Comentarios de Ajuste',
            'TieReaFecReg': 'Fecha de Registro',
            'TieReaEstReg': 'Estado de Registro',
        }

    def __init__(self, *args, **kwargs):
        super(TiemposRealesForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['TieReaFecReg'].initial = datetime.date.today()
            self.fields['TieReaEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['TieReaCod'].widget.attrs['readonly'] = True


class PlantillaActividadesForm(forms.ModelForm):
    class Meta:
        model = PlantillaActividades
        fields = ['PlaActCod', 'PlaActNom', 'PlaActDes', 'PlaActTipProCod', 'PlaActEstReg']
        widgets = {
            'PlaActCod': forms.TextInput(attrs={'class': 'form-control'}),
            'PlaActNom': forms.TextInput(attrs={'class': 'form-control'}),
            'PlaActDes': forms.Textarea(attrs={'class': 'form-control'}),
            'PlaActTipProCod': forms.Select(attrs={'class': 'form-control'}),
            'PlaActEstReg': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'PlaActCod': 'Código',
            'PlaActNom': 'Nombre',
            'PlaActDes': 'Descripción',
            'PlaActTipProCod': 'Tipo de Proyecto',
            'PlaActEstReg': 'Estado de Registro',
        }

    def __init__(self, *args, **kwargs):
        super(PlantillaActividadesForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo para nuevos registros
            self.fields['PlaActEstReg'].initial = EstadoRegistro.objects.get(EstRegNom='Activo')
        else:
            self.fields['PlaActCod'].widget.attrs['readonly'] = True
        