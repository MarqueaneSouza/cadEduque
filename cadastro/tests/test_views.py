import pytest
from django.urls import reverse
from cadastro.models import Professor, Funcao


@pytest.mark.django_db
def test_add_professor_view(client):
    # Preparação dos dados para a requisição POST
    post_data = {
        "nome": "João",
        "sobrenome": "Silva",
        "cargo": "Professor",
        "matricula": "1234",
        "funcao": ["Coordenador"],
        "lotação": ["Adélia"],
        "turno": ["Manhã"]
    }
    
    # Simula uma requisição POST para a view add_professor
    response = client.post(reverse('cadastro:cadastro'), post_data)
    
    # Verifica se o status da resposta é  200 OK
    assert response.status_code ==  200
    
    # Verifica se um novo professor foi criado
    assert Professor.objects.count() ==  1
    
    # Recupera o professor criado
    professor = Professor.objects.first()
    
    # Verifica se os campos do professor correspondem aos dados enviados
    assert professor.nome == post_data['nome']
    assert professor.sobrenome == post_data['sobrenome']
    assert professor.cargo == post_data['cargo']
    assert professor.matricula == post_data['matricula']
    
    # Verifica se as funções foram associadas ao professor
    assert Funcao.objects.filter(professor=professor).count() == len(post_data['funcao'])

