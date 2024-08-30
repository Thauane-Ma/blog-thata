from django.contrib import admin 
from .models import *


@admin.register (Curso) 
class CursoAdmin(admin.ModelAdmin):
    list_display = ['bolsa','link_certificado', 'data_conclusao', 'data_inicio', 'descricao', 'instituicao','nome', 'bolsa']
@admin.register (Perfil) 
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome','idade', 'cpf', 'email', 'telefone', 'endereco','data_nascimento', 'bio', 'foto_perfil']


# Register your models here.
