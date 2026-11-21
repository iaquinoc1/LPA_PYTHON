while True:
	try:
		x = int(input('Digite um número inteiro: '))
		break
	except ValueError: #Erro de valor
		print ("Oops, número inválido! Try again!")
	finally:
		print ("Obrigado")

i = 0
while True:
    try:
        nome = input('Por favor digite o seu nome: ')
        ind = int(input('Digite um índice do seu nome digitado: '))
        print(nome[ind])
        break
    except ValueError:
        print('Oops! Nome inválido. Tente novamente...')
    except IndexError: #Erro de índice
        print('Oops! índice inválido. Tente novamente...')
    finally: #Executa sempre!!
        print(f'Tentativa {i}')
        i += 1

#except: (sem valor) >> tratamento de erro genérico