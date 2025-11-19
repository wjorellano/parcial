from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="departamentos")
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} — {self.empresa.nombre}"

class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name="empleados")
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre

class Activo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name="activos")
    serial = models.CharField(max_length=120, unique=True)
    descripcion = models.CharField(max_length=250)
    fecha_adquisicion = models.DateField()

    def __str__(self):
        return f"{self.serial} ({self.descripcion})"
