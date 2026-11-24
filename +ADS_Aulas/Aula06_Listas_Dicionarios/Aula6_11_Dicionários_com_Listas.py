#Dicionário com listas dentro
#Cada linha do dicionário possui uma lista com todos os valores separados por aspas

games = {'nome':['Super Mario', 'Zelda Ocarina of Time','Pokemon Yellow'],
         'videogame':['Super Nintendo','Nintendo 64','Game Boy'],
         'ano':[1990,1998,1999]}
print(games)

games = {'nome':[],'videogame':[],'ano':[]} #Criando um dicionário vazio com 3 listas vazias
for i in range(1): #Laço/iteração com input para inserir os valores de cada lista
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video-game ele foi lançado?')
    ano = input('Qual o ano de lançamento?')
    games['nome'].append(nome) #Métodos (append) para inserir os valores nas listas
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)