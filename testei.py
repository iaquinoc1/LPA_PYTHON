def cadastrar_senha():
    senha = input("Digite uma senha: ")

    confirmacao = input("Confirme a senha: ")
    while senha != confirmacao:
        confirmacao = input("Confirme a senha: ")

        if senha != confirmacao:
            print("As senhas não são iguais. Tente novamente.")

    return senha


senha_cadastrada = cadastrar_senha()

print("Senha cadastrada com sucesso!")