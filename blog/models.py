from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_conclusao = models.DateField()
    link_certificado = models.URLField(blank=True, null=True)
    bolsa = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.instituicao}"


class Perfil(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField()
    bio = models.TextField(blank=True, null=True)  # Breve biografia ou descrição pessoal
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return self.nome





# Create your models here.
