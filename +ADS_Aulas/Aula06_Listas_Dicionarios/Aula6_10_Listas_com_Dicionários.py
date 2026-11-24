#Listas com dicionários
#A atribuição após a lista de dicionários insere todos dentro da lista

games = [] #Lista vazia
game1 = {'nome':'Super Mario', #Dicionário 1
         'videogame':'Super Nintendo',
         'ano':1990}
game2 = {'nome':'Zelda Ocarina of Time', #Dicionário 2
         'videogame':'Nintendo 64',
         'ano':1998}
game3 = {'nome':'Pokemon Yellow', #Dicionário 3
         'videogame':'Game Boy',
         'ano':1999}
games = [game1, game2, game3] #Insere os dicionários dentro da lista
print(games)

print (' ')

game = {} #Dicionário vazio
games = [] #Lista vazia

for i in range(1): #Laço programado para 1 entrada
    game['nome'] = input('Qual o nome do jogo?')
    game['videogame'] = input('Para qual video-game ele foi lançado?')
    game['ano'] = input('Qual o ano de lançamento?')
    games.append(game.copy()) #Método para copiar os dados para dentro do dicionário
print('-' * 20)
for jogos in games:
    for chave, valor in jogos.items():
        print(f'{chave} : {valor}')
#Método items para imprimir chaves e valores, com duas variáveis