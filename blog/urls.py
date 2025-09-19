from django.urls import path
from blog.views import (
    lista_publicaciones,
    detalle_publicacion,
    crear_publicacion
)

urlpatterns = [
    path('', lista_publicaciones, name='lista_publicaciones'),
    path('nueva/', crear_publicacion, name='crear_publicacion'),
    path('<slug:slug>/', detalle_publicacion, name='detalle_publicacion'),
]