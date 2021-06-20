from django.shortcuts import render
from .models import Administrador
from .models import Beneficiario
from .models import Departamento
from .models import Entidad
from .models import Municipio
from .models import Paquete
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return render(request, "Principal/index.html")

@login_required
def lista(request):
	beneficiarios = Beneficiario.objects.all()
	contexto = {
		'beneficiarios':beneficiarios
	}
	return render(request,"Principal/lista.html",contexto)

@login_required
def verBeneficiario(request):
	return render(request,"Principal/verBene.html")





