from flask import Flask, request
from flask_cors import CORS
import json

"""
pip install flask
pip install flask-cors
"""

app = Flask(__name__)
# CORS(app)  # -> Permite CORS para todas as rotas
CORS(app, supports_credentials=True, methods=["GET", "POST"])  # -> Permite os metodos GET e POST
# CORS(app, origins=['https://meusite.com', 'http://outrosite.com'], headers=['Content-Type', 'Authorization'])


@app.route('/')
def home():
    return 'Hello World'


# Exemplo: http://127.0.0.1:5000/user/{"name": "Witor"}
@app.route('/user/<info>')
def user(info):
    data = json.loads(info)  # -> Transforma uma String JSON em um Dicionario Python.
    print(data)
    print(type(data))
    return f'Seu nome é {data["name"]}'


# Exemplo: http://127.0.0.1:5000/admin?data={"name": "Renato"}
@app.route('/admin')
def admin():
    data = request.args.get('data')
    data_dict = json.loads(data)  # -> Transforma uma String JSON em um Dicionario Python.
    print(data_dict)
    print(type(data_dict))
    return f'Seu nome é {data_dict["name"]}'


# Exemplo: http://127.0.0.1:5000/endpoint
@app.route('/endpoint', methods=['POST'])
def enviar_usuario():
    teste = 2
    if teste == 1:
        print('Request com Data')
        data = request.data
        print(data)  # -> b'{\r\n    "name": "Patrick"\r\n}'
        print(type(data))  # -> <class 'bytes'>
        data_dict = json.loads(data)
        print(data_dict)  # -> {'name': 'Patrick'}
        return f'O JSON recebido é: {data_dict}'
    else:
        print('Request com JSON')
        other_data = request.json
        print(other_data)  # -> {'name': 'Patrick'}
        return f'O JSON recebido é: {other_data}'


app.run()
