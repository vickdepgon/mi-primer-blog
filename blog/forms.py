from django import forms
from .models import Publicacion
class FormPublicacion(forms.ModelForm):
  class Meta:
    model = Publicacion
    fields = ('titulo', 'texto',)
