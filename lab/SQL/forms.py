from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    CliFecIng = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    CliFecCes = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}), required=False)
    class Meta:
        model = Cliente
        fields = ['CliCod', 'CliNom', 'CliTip', 'CliFecIng', 'CliFecCes', 'CliEst', 'CliEstReg']
