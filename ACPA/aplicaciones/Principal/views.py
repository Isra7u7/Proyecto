from django.http import JsonResponse                                     #???
from django.shortcuts import render, redirect, get_object_or_404
from .models import Beneficiario
from .models import Departamento
from .models import Entidad
from .models import Municipio
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BeneficiarioForm, CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

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

#Función de la pantalla de creación de beneficiarios 1
def crearBeneficiario(request):
    form = BeneficiarioForm()
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear')
    return render(request, 'Principal/crear_beneficiario.html', {'form': form})

#Función de la pantalla de creación de beneficiarios 2

def crearBeneficiario_update(request, pk):
    beneficiario = get_object_or_404(Beneficiario, pk=pk)
    form = BeneficiarioForm(instance=beneficiario)
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST, instance=beneficiario)
        if form.is_valid():
            form.save()
            return redirect('crear_change', pk=pk)
    return render(request, 'Principal/crear_beneficiario.html', {'form': form})

#Función de la pantalla de creación de beneficiarios 3
# AJAX
def load_municipios(request):
    departamento_id = request.GET.get('departamento_id')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).all()
    return render(request, 'Principal/municipios_dropdown.html', {'municipios': municipios})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


#Funcion para eliminar un registro
def eliminarBeneficiario(request, ID_BENEFICIARIO):
	beneficiario = Beneficiario.objects.get(ID_BENEFICIARIO = ID_BENEFICIARIO)
	beneficiario.delete()
	return redirect('/lista')

#Funcion para editar
def editarBeneficiario(request, ID_BENEFICIARIO):
    beneficiario = get_object_or_404(Beneficiario, ID_BENEFICIARIO =ID_BENEFICIARIO)
    data = {
        'form':BeneficiarioForm(instance = beneficiario)
    }
    return render(request, "Principal/editar_beneficiario.html", data)

@login_required
def verBeneficiario(request):
	return render(request,"Principal/verBene.html")




@login_required
def registro_usuario(request):
   data = { 'form' : CustomUserForm()
   }
      
   if request.method == 'POST':
       formulario = CustomUserForm(request.POST)
       if formulario.is_valid():
            formulario.save()
           #autenticar 
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            email = formulario.cleaned_data['email']
            user = authenticate(username= username, password= password)
            
            return redirect(to='/')

   return render(request,'registration/registrar.html', data)    






