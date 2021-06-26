from django import forms
from .models import Beneficiario, Municipio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

       
        self.fields['municipio'].queryset = Municipio.objects.none()

       
        if 'departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('NOMBRE_DEPARTAMENTO')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('NOMBRE_DEPARTAMENTO')


        #seleccion = bool(self.data.get('RECEPTOR_BENEFICIARIO'))
        
        """
        #if self.data.get('RECEPTOR_BENEFICIARIO') == False:
        if self.BooleanField['RECEPTOR_BENEFICIARIO'] == True:
            self.fields['entidad'].widget.attrs.update({'disabled': False})
            self.fields['CANTIDAD'].widget.attrs.update({'disabled': False})
        else:
            self.fields['entidad'].widget.attrs.update({'disabled': True}) #?????
            self.fields['CANTIDAD'].widget.attrs.update({'disabled': True}) #?????
"""


class CustomUserForm(UserCreationForm):
     class Meta: 
           model = User
           fields = ['username', 'email' , 'password1', 'password2']
           help_texts = {
                  'username' : None,
                  'password2' : None
                  



            }