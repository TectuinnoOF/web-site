from django import forms
from .models import Publicacion
from tinymce.widgets import TinyMCE


class PublicacionForm(forms.ModelForm):
    contenido = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),
        label="Contenido"
    )

    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'publicado_en']