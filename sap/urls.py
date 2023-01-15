
"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from personas.views import detalle_persona, editar_persona, eliminar_persona, nueva_persona
from webapp.views import bienvenido
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido,name='inicio'),
    path('detalle_persona/<int:id>', detalle_persona),
    path('nueva_persona', nueva_persona),
    path('editar_persona/<int:id>', editar_persona),
    path('eliminar_persona/<int:id>', eliminar_persona)
]
