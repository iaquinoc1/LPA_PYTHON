senha = input('Digite uma senha: ')
tentativas = 0
limite = 3

while tentativas < limite:
    confirma = input('Confirme a senha: ')

    if senha == confirma:
        print('Senha OK')
        break
    else:
        tentativas += 1
        restantes = limite - tentativas
        print(f'Senhas não conferem. Tentativas restantes: {restantes}')

if tentativas == limite:
    print('Número máximo de tentativas excedido.')
