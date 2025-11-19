
from django.urls import path
from . import views

app_name = "administracion"

urlpatterns = [

    # EMPRESAS
    path("", views.EmpresaListView.as_view(), name="empresa_list"),
    path("empresas/nuevo/", views.EmpresaCreateView.as_view(), name="empresa_create"),
    path("empresas/<int:pk>/editar/", views.EmpresaUpdateView.as_view(), name="empresa_update"),
    path("empresas/<int:pk>/borrar/", views.EmpresaDeleteView.as_view(), name="empresa_delete"),

    # DEPARTAMENTOS
    path("departamentos/", views.DepartamentoListView.as_view(), name="departamento_list"),
    path("departamentos/nuevo/", views.DepartamentoCreateView.as_view(), name="departamento_create"),
    path("departamentos/<int:pk>/editar/", views.DepartamentoUpdateView.as_view(), name="departamento_update"),
    path("departamentos/<int:pk>/borrar/", views.DepartamentoDeleteView.as_view(), name="departamento_delete"),

    # EMPLEADOS
    path("empleados/", views.EmpleadoListView.as_view(), name="empleado_list"),
    path("empleados/nuevo/", views.EmpleadoCreateView.as_view(), name="empleado_create"),
    path("empleados/<int:pk>/editar/", views.EmpleadoUpdateView.as_view(), name="empleado_update"),
    path("empleados/<int:pk>/borrar/", views.EmpleadoDeleteView.as_view(), name="empleado_delete"),

    # ACTIVOS
    path("activos/", views.ActivoListView.as_view(), name="activo_list"),
    path("activos/nuevo/", views.ActivoCreateView.as_view(), name="activo_create"),
    path("activos/<int:pk>/editar/", views.ActivoUpdateView.as_view(), name="activo_update"),
    path("activos/<int:pk>/borrar/", views.ActivoDeleteView.as_view(), name="activo_delete"),

]
