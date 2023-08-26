from playwright.sync_api import sync_playwright
import time
from commom import *

def create_account(nome, senha):
    with sync_playwright() as p:
        email = generate_random_word(4)+'@yopmail.com'
        browser = p.chromium.launch(headless=False)
        cadastro = browser.new_page()
        cadastro.goto("https://front.serverest.dev/cadastrarusuarios")
        cadastro.locator('//*[@id="nome"]').fill(nome)
        cadastro.locator('//*[@id="email"]').fill(email)
        cadastro.locator('//*[@id="password"]').fill(senha)
        cadastro.locator('xpath=//*[@id="root"]/div/div/form/div[5]/button').click()
        return(email)

def login_serve_rest(email, senha):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        pagina = browser.new_page()
        pagina.goto("https://front.serverest.dev/login")
        pagina.locator('xpath=//*[@id="email"]').click()
        pagina.locator('xpath=//*[@id="email"]').fill(email)
        pagina.locator('xpath=//*[@id="password"]').fill(senha)
        pagina.locator('xpath=//*[@id="root"]/div/div/form/button').click()


# Caso de teste 1: Criar uma conta no front do Serve Rest
nome = 'Carol Teste May'
senha = '123456'
email = create_account(nome, senha)

# Caso de teste 2: Criar uma conta e fazer o login no front do Serve Rest
login_serve_rest(email, senha)