import requests
import json
from commom import *

# Dados do usuário a ser criado
def create_account(nome, senha, create_user_url):
    email = generate_random_word(4)+'@yopmail.com'
    data = {
        "nome": nome,
        "email": email,
        "password": senha,
        "administrador": 'true'
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post(create_user_url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print("Cadastro realizado com sucesso")
        user_id = response.json().get('_id')
        print(f'ID do usuário criado: {user_id}')
        print(email)
        return (email)
    else:
        print("Este email já está sendo usado")
        print(response.status_code)
        print(response.text)

# Função para fazer login
def login_serve_rest(email, senha, login_url):
    data = {
        "email": email,
        "password": senha
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post(login_url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print("Login bem-sucedido!")
        token = response.json().get('authorization')
        print(f'Token de autorização: {token}')
    else:
        print("Falha no login.")
        print(response.status_code)
        print(response.text)

# Caso de teste 1: Criar uma conta no front do Serve Rest
nome = 'Carol Teste May'
senha = '123456'
create_user_url = 'https://serverest.dev/usuarios'
email = create_account(nome, senha, create_user_url)

# Caso de teste 2: Criar uma conta e fazer o login no front do Serve Rest
login_url = 'https://serverest.dev/login'
login_serve_rest(email, senha, login_url)
