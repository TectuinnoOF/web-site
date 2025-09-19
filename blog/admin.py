from django.contrib import admin
from .models import Publicacion
from django import forms
from tinymce.widgets import TinyMCE

# Register your models here.
class PublicacionAdminForm(forms.ModelForm):
    contenido = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Publicacion
        fields = '__all__'

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    form = PublicacionAdminForm
    list_display = ('titulo', 'autor', 'publicado_en', 'creado_en')
    list_filter = ('autor', 'publicado_en')
    search_fields = ('titulo', 'contenido')
    ordering = ('-publicado_en',)
