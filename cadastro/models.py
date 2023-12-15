from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=8)
    cargo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Funcao(models.Model):
    funcao = models.CharField(max_length=50)
    lotacao = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.funcao
