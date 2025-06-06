from selenium.webdriver.common.by import By

class LoginPage:
    name_input = (By.ID, "name")
    email_input = (By.ID, "email")
    birth_date_input = (By.ID, "birthDate")
    password_input = (By.ID, "password")
    password_confirm_input = (By.ID, "passwordConfirm")
    terms_checkbox = (By.ID, "terms")
    message_text = (By.ID, "mensagem")
    submit_button = (By.CSS_SELECTOR, "button.btn.btn-primary")