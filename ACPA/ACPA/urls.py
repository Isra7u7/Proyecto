"""ACPA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from aplicaciones.Principal import views
from aplicaciones.Principal.views import lista, verBeneficiario, eliminarBeneficiario, editarBeneficiario, crearBeneficiario, registro_usuario



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('lista/',views.lista),
    path('crear_beneficiario/', views.crearBeneficiario, name = 'crear'),
    path('<int:pk>/', views.crearBeneficiario_update, name='crear_change'),          
    path('ajax/load-municipios/', views.load_municipios, name='ajax_load_municipios'),
    path('verBeneficiario/',views.verBeneficiario),
    path('accounts/', include('django.contrib.auth.urls')),
    path('eliminar_beneficiario/<int:ID_BENEFICIARIO>/', views.eliminarBeneficiario, name = 'eliminar_beneficiario'),
    path('editar_beneficiario/<int:ID_BENEFICIARIO>/', views.editarBeneficiario, name = 'editar_beneficiario'),
    path('registro/', registro_usuario, name='registro_usuario'),
]

urlpatterns += staticfiles_urlpatterns()
