from django import forms
from .models import Empresa, Departamento, Empleado, Activo

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = "__all__"

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = "__all__"
