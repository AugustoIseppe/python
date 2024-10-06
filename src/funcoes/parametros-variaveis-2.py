import secrets
from datetime import datetime


def criar_usuario(**atributos):
    novo_usuario = {
        "nome": "",
        "email": "",
        "senha": secrets.token_urlsafe(20),
        "data_criacao": datetime.now(),
        "ativo": True
    }

    novo_usuario.update(atributos)
    return novo_usuario


novo_usuario = criar_usuario(
    nome="Augusto Iseppe",
    email="augusto.iseppe@empresa.com.br"
)

print(novo_usuario)
