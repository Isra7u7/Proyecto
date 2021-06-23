from django.contrib import admin
from .models import Beneficiario
from .models import Departamento
from .models import Entidad
from .models import Municipio

# Register your models here.

admin.site.register(Beneficiario)
admin.site.register(Departamento)
admin.site.register(Entidad)
admin.site.register(Municipio)