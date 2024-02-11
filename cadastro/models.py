from django.db import models

CHOICES_CARGO = [
    ('', 'Selecione um cargo'),
    ('peb', 'Professor de Séries Inicias'),
    ('aee', 'Professor de Atendimento Educacional Especializado'),
    ('apoio', 'Professor de Apoio Pedagógico'),
    ('português', 'PEB - Língua Portuguesa'),
    ('matemática', 'PEB - Matemática'),
    ('geografia', 'PEB - Geografia'),
    ('ciências', 'PEB - Ciências'),
    ('ed_fisica', 'PEB - Ed. Física'),
    ('arte', 'PEB - Arte'),
    ('ed_religiosa', 'PEB - Educação Religiosa'),
    ('ingles', 'PEB - Língua Inglesa'),
    ('musica', 'Professor de Música'),
]

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=8, unique=True)
    cargo = models.CharField(choices=CHOICES_CARGO,default="", max_length=50)

    def __str__(self) -> str:
        return self.nome


class Funcao(models.Model):
    funcao = models.CharField(max_length=50)
    lotacao = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.funcao

