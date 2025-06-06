Feature: Cadastro de usuário
    Scenario: Preenchimento e envio do formulário
    Given o usuário está na página de login
    When ele preenche usuário e senha válidos
    Then ele vê a mensagem de sucesso e finaliza o teste