from django.contrib import admin
from .models import Administrador
from .models import Beneficiario
from .models import Departamento
from .models import Entidad
from .models import Municipio
from .models import Paquete

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Beneficiario)
admin.site.register(Departamento)
admin.site.register(Entidad)
admin.site.register(Municipio)
admin.site.register(Paquete)