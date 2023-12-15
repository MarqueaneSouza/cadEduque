from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro, Funcao

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cargo = request.POST.get('cargo')
        funcao = request.POST.getlist('funcao')
        lotacao = request.POST.getlist('lotação')
        turno = request.POST.getlist('turno')

    # adiciona no banco de dados
        cadastro = Cadastro(
            nome = nome,
            sobrenome = sobrenome,
            cargo = cargo
        )

        cadastro.save()

        for funcao, lotacao, turno in zip(funcao, lotacao, turno):
            func = Funcao(funcao=funcao, lotacao=lotacao, turno=turno, cadastro=cadastro)
            func.save()

        return HttpResponse('teste')