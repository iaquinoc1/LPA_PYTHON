senha = input('Digite uma senha: ')
confirma = input ('Confirme a senha')
while senha != confirma:
    print ('Senhas não conferem')
    confirma = input ('Confirme a senha')
else:
    print ('Senha OK')