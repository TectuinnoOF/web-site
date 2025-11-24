from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from blog.models import Publicacion
from django.contrib.auth.models import Group
from .forms import UserCreationForm, RegistroForm
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
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Asignar grupo
            grupo, created = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo)

            return redirect("/")
    else:
        form = RegistroForm()

    return render(request, 'ide/register_clients.html', {'form': form})