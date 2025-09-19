from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, unique=True, verbose_name='Titulo')
    slug = models.SlugField(max_length=220, unique=True, blank=True, editable=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', verbose_name='Autor' )
    contenido = models.TextField(verbose_name='Contenido')
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')
    publicado_en = models.DateTimeField(default=timezone.now, verbose_name='Fecha de publicacion')

    class Meta:
        ordering = ['-publicado_en']
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["creado_en"])
        ]
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
