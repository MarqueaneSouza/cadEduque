from django.shortcuts import render
from django.http import HttpResponse

from cadastro.professor_form import FormProfessor
from .models import Professor, Funcao


def add_professor(request):
    if request.method == "GET":
        # Se for uma requisição GET, renderiza o formulário de cadastro
        return render(request, "cadastro/cadastro.html", {'form':FormProfessor()})
    elif request.method == "POST":
        # Se for uma requisição POST, obtém os dados do formulário
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        cargo = request.POST.get("cargo")
        matricula = request.POST.get("matricula")
        funcoes = request.POST.getlist("funcao")
        lotacoes = request.POST.getlist("lotação")
        turnos = request.POST.getlist("turno")

        # Validação Matrícula
        professor = Professor.objects.filter(matricula=matricula)

        if professor.exists():
            return render(
                request,
                "cadastro/cadastro.html",
                {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "cargo": cargo,
                    "funcoes": (funcoes, lotacoes, turnos),
                    'form':FormProfessor()
                },
               
            )

        # Adiciona um novo professor no banco de dados
        professor = Professor(
            nome=nome, sobrenome=sobrenome, cargo=cargo, matricula=matricula
        )
        # Salva o professor no banco de dados
        professor.save()

        # zip: cria uma tupla, dentro de uma lista que co-relaciona informações
        for funcao, lotacao, turno in zip(funcoes, lotacoes, turnos):
            func = Funcao(
                funcao=funcao, lotacao=lotacao, turno=turno, professor=professor
            )
            func.save()

        # Retorna uma resposta HTTP simples indicando sucesso (pode ser personalizado)
        return HttpResponse("Cadastro realizado com sucesso")
