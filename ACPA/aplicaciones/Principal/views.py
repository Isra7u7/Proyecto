from django.shortcuts import render
from .models import Administrador
from .models import Beneficiario
from .models import Departamento
from .models import Entidad
from .models import Municipio
from .models import Paquete

# Create your views here.

def index(request):
	return render(request, "Principal/index.html")


def lista(request):
	beneficiarios = Beneficiario.objects.all()
	contexto = {
		'beneficiarios':beneficiarios
	}
	return render(request,"Principal/lista.html",contexto)


