from django.db import models

# Create your models here.

BOOL_CHOICES = ((True, 'Si'), (False, 'No'))

class Departamento(models.Model):
	#ID_DEPARTAMENTO = models.CharField(max_length = 5, primary_key = True)
	NOMBRE_DEPARTAMENTO = models.CharField(max_length = 30)

	def __str__(self):
		return self.NOMBRE_DEPARTAMENTO

class Entidad(models.Model):
	#ID_ENTIDAD = models.CharField(max_length = 5, primary_key = True)
	NOMBRE_ENTIDAD = models.CharField(max_length = 25)

	def __str__(self):
		return self.NOMBRE_ENTIDAD

class Municipio(models.Model):
	#ID_MUNICIPIO = models.CharField(max_length = 5, primary_key = True)
	departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
	NOMBRE_MUNICIPIO = models.CharField(max_length = 30)

	def __str__(self):
		return self.NOMBRE_MUNICIPIO

class Beneficiario(models.Model):
	ID_BENEFICIARIO = models.AutoField(primary_key = True)
	DUI_BENEFICIARIO = models.CharField(max_length = 10)
	NOMBRE_BENEFICIARIO = models.CharField(max_length = 20)
	APELLIDO_BENEFICIARIO = models.CharField(max_length = 20)
	departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
	DIRECCION_BENEFICIARIO = models.CharField(max_length = 100)
	RECEPTOR_BENEFICIARIO = models.BooleanField(choices = BOOL_CHOICES)
	entidad = models.ForeignKey(Entidad, on_delete=models.SET_NULL, blank=True, null=True)
	CANTIDAD = models.IntegerField()

	def __str__(self):
		return self.NOMBRE_BENEFICIARIO