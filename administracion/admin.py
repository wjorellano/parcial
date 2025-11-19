from django.contrib import admin
from .models import Empresa, Departamento, Empleado, Activo

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nit", "direccion")
    search_fields = ("nombre", "nit")

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa")
    list_filter = ("empresa",)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "departamento", "fecha_ingreso")
    list_filter = ("departamento__empresa",)

@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    list_display = ("serial", "descripcion", "empleado", "fecha_adquisicion")
    search_fields = ("serial", "descripcion")
