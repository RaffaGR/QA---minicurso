import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from features.pages.login_page import LoginPage

class LoginActions:
    def __init__(self, driver):
        self.driver = driver

    def fill_all_fields(self):
        # Espera pelo campo "Nome" e preenche
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPage.name_input)
        ).send_keys("Tester")

        # Preenche o campo "E-mail"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPage.email_input)
        ).send_keys("teste@example.com")

        # Preenche o campo "Data de nascimento" (formato YYYY-MM-DD)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPage.birth_date_input)
        ).send_keys("06/06/2000")

        # Preenche o campo "Senha"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPage.password_input)
        ).send_keys("SenhaForte123!")

        # Preenche o campo "Confirmar Senha"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginPage.password_confirm_input)
        ).send_keys("SenhaForte123!")

        # Marca o checkbox de "Concordo com os Termos"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPage.terms_checkbox)
        ).click()

        # Após preencher tudo, clica no botão de submit
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPage.submit_button)
        ).click()
        time.sleep(2)  # tempo para a mensagem aparecer

    def click_on_submit(self):
        # Aguarda o botão de submit estar clicável e então clica
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPage.submit_button)
        ).click()
        time.sleep(10)
