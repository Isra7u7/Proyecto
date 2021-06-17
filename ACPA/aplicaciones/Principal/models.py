from django.db import models

# Create your models here.

BOOL_CHOICES = ((True, 'Si'), (False, 'No'))

class Administrador(models.Model):
	DUI_ADMINISTRADOR = models.CharField(max_length = 10, primary_key = True)
	CONTRASENA_ADMINISTRADOR = models.CharField(max_length = 20)

class Beneficiario(models.Model):
	ID_BENEFICIARIO = models.AutoField(primary_key = True)
	DUI_BENEFICIARIO = models.CharField(max_length = 10)
	NOMBRE_BENEFICIARIO = models.CharField(max_length = 20)
	APELLIDO_BENEFICIARIO = models.CharField(max_length = 20)
	DEPARTAMENTO_BENEFICIARIO = models.CharField(max_length = 30)
	MUNICIPIO_BENEFICIARIO = models.CharField(max_length = 30)
	DIRECCION_BENEFICIARIO = models.CharField(max_length = 100)
	RECEPTOR_BENEFICIARIO = models.BooleanField(choices = BOOL_CHOICES)
	ENTIDAD_BENEFICIARIO = models.CharField(max_length = 25)

class Departamento(models.Model):
	ID_DEPARTAMENTO = models.CharField(max_length = 5, primary_key = True)
	NOMBRE_DEPARTAMENTO = models.CharField(max_length = 30)

class Entidad(models.Model):
	ID_ENTIDAD = models.AutoField(primary_key = True)
	NOMBRE_ENTIDAD = models.CharField(max_length = 25)

class Municipio(models.Model):
	ID_MUNICIPIO = models.CharField(max_length = 5, primary_key = True)
	ID_DEPARTAMENTO = models.ForeignKey(Departamento, on_delete = models.CASCADE)
	NOMBRE_MUNICIPIO = models.CharField(max_length = 30)

class Paquete(models.Model):
	ID_PAQUETE = models.AutoField(primary_key = True)
	ID_ENTIDAD = models.ForeignKey(Entidad, on_delete = models.CASCADE)
	ID_BENEFICIARIO = models.ForeignKey(Beneficiario, on_delete = models.CASCADE)
	ID_DEPARTAMENTO = models.ForeignKey(Departamento, on_delete = models.CASCADE)
	ID_MUNICIPIO = models.ForeignKey(Municipio, on_delete = models.CASCADE)
	CANTIDAD = models.IntegerField()


