def valida_int (pergunta, min, max): #Esta função valida o item escolhido no menu
	#Help da função:
	'''
	Esta função valida o item escolhido no menu
	:param pergunta: Pede pra selecionar o item do Menu
	:param min: Valor mínimo (1)
	:param max: Valor máximo (3)
	Menu com três opções
	'''
	x = int(input(pergunta))
	while((x < min) or (x > max)):
		x = int(input(pergunta))
	return x

#Manipulação de arquivos:
#r - leitura
#a - escrita
#w - escrita (sobreescreve conteúdo)
#+ - atualização (leitura e escrita)
#b - mode binário

def existeArquivo (nomeArquivo): #Esta função identifica se o arquivo já existe
	try:
		a = open(nomeArquivo, 'rt') #sempre tem um 't' depois do modo
		a.close() #Sempre fechar o arquivo!
	except FileNotFoundError: #tratamento de exceção
		return False
	else:
		return True

def criarArquivo(nomeArquivo): #Esta função serve para criar um arquivo
	try:
		a = open(nomeArquivo, 'wt+') #sempre tem um 't' depois do modo
		a.close() #Sempre fechar o arquivo!
	except: #tratamento de exceção
		print("Erro na criação do arquivo")
	else:
		print(f'Arquivo {nomeArquivo} criado com sucesso')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame): #Esta função serve para cadastrar um novo jogo
	try:
		a = open(nomeArquivo, 'at') #sempre tem um 't' depois do modo
	except: #tratamento de exceção
		print('Erro ao abrir o arquivo')
	else:
		a.write(f'{nomeJogo}; {nomeVideogame}\n')
	finally: #finally executa sempre, mas nem sempre é necessário
		a.close() #Sempre fechar o arquivo!

def listarArquivo(nomeArquivo): #Esta função serve para listar os jogos cadastrados
	try:
		a = open(nomeArquivo, 'rt') #sempre tem um 't' depois do modo
	except: #tratamento de exceção
		print('Erro ao ler o arquivo')
	else:
		print(a.read())
	finally:
		a.close() #Sempre fechar o arquivo!

#Programa principal inicia aqui
arquivo = 'games.txt'
if existeArquivo(arquivo):
	print('Arquivo localizado')
else:
	print('Arquivo inexistente')
	criarArquivo (arquivo)

while True:
	print('Menu')
	print('1 - Cadastrar novo item')
	print('2 - Listar itens cadastrados')
	print('3 - Sair')

	op = valida_int('Escolha a opção desejada: ', 1, 3)
	if (op == 1): #Novo item
		print('Opção de cadastro selecionada...\n')
		nomeJogo = input('Nome do jogo: ')
		nomeVideogame = input('Nome do videogame: ')
		cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
		print('Novo jogo cadastrado!')

	elif (op ==2): #Listar
		print('Opção de listar selecionada...\n')
		listarArquivo(arquivo)

	elif (op == 3):
		print('Encerrando o programa...')
		break