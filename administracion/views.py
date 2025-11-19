# administracion/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Empresa, Departamento, Empleado, Activo
from .forms import EmpresaForm, DepartamentoForm, EmpleadoForm, ActivoForm

# -----------------------------
# EMPRESAS
# -----------------------------
class EmpresaListView(ListView):
    model = Empresa
    template_name = "administracion/empresa_list.html"
    context_object_name = "empresas"

class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = "administracion/empresa_form.html"
    success_url = reverse_lazy("administracion:empresa_list")

class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = "administracion/empresa_form.html"
    success_url = reverse_lazy("administracion:empresa_list")

class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = "administracion/empresa_confirm_delete.html"
    success_url = reverse_lazy("administracion:empresa_list")

# =============================
# DEPARTAMENTOS (CRUD completo)
# =============================

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "administracion/departamento_list.html"
    context_object_name = "departamentos"

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "administracion/departamento_form.html"
    success_url = reverse_lazy("administracion:departamento_list")

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "administracion/departamento_form.html"
    success_url = reverse_lazy("administracion:departamento_list")

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = "administracion/departamento_confirm_delete.html"
    success_url = reverse_lazy("administracion:departamento_list")

# =============================
# EMPLEADOS (CRUD completo)
# =============================

class EmpleadoListView(ListView):
    model = Empleado
    template_name = "administracion/empleado_list.html"
    context_object_name = "empleados"

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "administracion/empleado_form.html"
    success_url = reverse_lazy("administracion:empleado_list")

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "administracion/empleado_form.html"
    success_url = reverse_lazy("administracion:empleado_list")

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "administracion/empleado_confirm_delete.html"
    success_url = reverse_lazy("administracion:empleado_list")

# =============================
# ACTIVOS (CRUD completo)
# =============================

class ActivoListView(ListView):
    model = Activo
    template_name = "administracion/activo_list.html"
    context_object_name = "activos"

class ActivoCreateView(CreateView):
    model = Activo
    form_class = ActivoForm
    template_name = "administracion/activo_form.html"
    success_url = reverse_lazy("administracion:activo_list")

class ActivoUpdateView(UpdateView):
    model = Activo
    form_class = ActivoForm
    template_name = "administracion/activo_form.html"
    success_url = reverse_lazy("administracion:activo_list")

class ActivoDeleteView(DeleteView):
    model = Activo
    template_name = "administracion/activo_confirm_delete.html"
    success_url = reverse_lazy("administracion:activo_list")
