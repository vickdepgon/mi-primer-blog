from django.contrib import admin
from .models import Publicacion #hace referencia a la clase anterior


admin.site.register(Publicacion)#se registra el modelo que hicimos
