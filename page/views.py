from django.shortcuts import render
from blog.models import Publicacion
# Create your views here.
def index(request):
    publicaciones = Publicacion.objects.order_by('-creado_en')[:3]
    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'page/index.html', context)

def ide_page(request):
    return render(request, 'ide/ide.html')

def register_clients(request):
    return render(request, 'ide/register_clients.html')