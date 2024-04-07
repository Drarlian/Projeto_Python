import requests
import json


def utilizando_get():
    # URL para fazer a requisição GET
    url = 'http://localhost:8000/usuarios'

    # Faz a requisição GET
    response = requests.get(url)

    # Verifica se a requisição foi bem sucedida (código 200)
    if response.status_code == 200:
        # Exibe o conteúdo da resposta
        print(response.json())
    else:
        # Exibe uma mensagem de erro caso a requisição não tenha sido bem sucedida
        print('Erro:', response.status_code)


def utilizando_post():
    # URL para fazer a requisição POST:
    url = 'http://localhost:8000/cadastrar-usuario'

    response = requests.post(url, json={"nome": "renato", "idade": 22, "email": "renato@email.com"})
    print(response.json())


# utilizando_get()
# utilizando_post()
