from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.forms import PublicacionForm
from blog.models import Publicacion

# Create your views here.
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'blog/lista_publicaciones.html', context)

def detalle_publicacion(request, slug):
    publicacion = get_object_or_404(Publicacion, slug=slug)
    context = {
        'publicacion': publicacion
    }
    return render(request, 'blog/detalle_publicacion.html', context)

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.creado_en = timezone.now()
            publicacion.save()
            return redirect("detalle_publicacion", slug=publicacion.slug)
    else:
        form = PublicacionForm()

    context = {
        'form': form
    }
    return render(request, 'blog/form_publicacion.html', context)