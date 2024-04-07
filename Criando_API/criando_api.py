from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

usuarios: List[dict[str, int | str]] = [{"nome": "Witor", "idade": 20, "email": "witor@email.com"},
                                        {"nome": "Patrick", "idade": 26, "email": "patrick@email.com"},
                                        {"nome": "Diana", "idade": 28, "email": "diana@email.com"},
                                        {"nome": "Duda", "idade": 28, "email": "duda@email.com"}]


class Usuario(BaseModel):
    nome: str
    idade: int
    email: str


@app.get('/usuarios')
def pegar_usuarios():
    return usuarios


@app.post('/cadastrar-usuario')
def cadastrar_usuario(usuario: Usuario):
    try:
        usuarios.append({"nome": usuario.nome, "idade": usuario.idade, "email": usuario.email})
    except:
        return HTTPException(522)
    return {'status': 200, 'msg': 'Usuario cadastrado com sucesso!'}
