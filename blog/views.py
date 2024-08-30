from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    informacoes = Perfil.objects.all()
    contexto = {
        'sobre': informacoes,
    }
    return render(request, 'index.html', contexto)

def academico(request):
    return render(request, 'academico.html')
