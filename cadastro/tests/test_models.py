import pytest
from django.db.utils import IntegrityError
from cadastro.models import Funcao, Professor

@pytest.mark.django_db
def test_criar_professor_e_str():
    # Dados de exemplo para criar um Professor
    dados_professor = {
        'nome': 'João',
        'sobrenome': 'Silva',
        'matricula': '1234',
        'cargo': 'peb',
    }

    # Criação de um Professor
    professor = Professor.objects.create(**dados_professor)

    # Assert para verificar se o Professor foi criado corretamente
    assert professor.nome == dados_professor['nome']
    assert professor.sobrenome == dados_professor['sobrenome']
    assert professor.matricula == dados_professor['matricula']
    assert professor.cargo == dados_professor['cargo']

    # Assert para verificar se o método __str__ está implementado corretamente
    assert str(professor) == 'João'

# TESTS FUNCAO
def test_str_metodo_funcao():
    # Dados de exemplo para criar uma Funcao
    dados_funcao = {
        'funcao': 'Coordenador',
        'lotacao': 'Adélia',
        'turno': 'Manhã',
        'professor': Professor.objects.create(nome='Alice', sobrenome='Silva', matricula='5678', cargo='peb'),
    }

    # Criação de uma Funcao
    funcao = Funcao.objects.create(**dados_funcao)

    # Assert para verificar se o método __str__ está implementado corretamente
    assert str(funcao) == 'Coordenador'