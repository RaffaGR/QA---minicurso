from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.actions.login_actions import LoginActions
from features.pages.login_page import LoginPage

@given("o usuário está na página de login")
def step_abre_pagina_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://paulohlsena.github.io/formulario-testes/")
    context.login = LoginActions(context.driver)

@when("ele preenche usuário e senha válidos")
def step_preenche_credenciais(context):
    context.login.fill_all_fields()

@then("ele vê a mensagem de sucesso e finaliza o teste")
def step_verifica_mensagem_sucesso(context):
    # Espera a mensagem de sucesso aparecer
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(LoginPage.message_text)
    )
    # Captura o texto exibido
    mensagem = context.driver.find_element(*LoginPage.message_text).text
    # Verifica se é exatamente o texto esperado
    assert mensagem == "Cadastro realizado com sucesso!"
    # Finaliza o navegador
    context.driver.quit()
