#Dicionários:
#Estrutura de dados dinâmica
#Permite alterar dados e tamanho
#Indexados por chaves (palavras-chave)
#Representados por chaves {}

mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
print('Tupla: ', mochila)

mochila = ['Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos']
print('Lista: ', mochila)

mochila = {'Laptop':1, 'Smartphone':2, 'Power Bank':3, 'Carregadores e Cabos':4}
print('Dicionário: ', mochila)

print (" ")

#Sempre uma dupla >> palavra-chave e valor

game = {'nome':'Super Mario', #Não esquecer da vírgula
		'desenvolvedora':'Nintendo', #Não esquecer da vírgula
		'ano':'1990'}
print (game)

#Nos dicionários não é possível buscar pelo índice, por isso é necessário utilizar keywords

print ("Game:", game['nome'])
print ("Estúdio:", game['desenvolvedora'])
print ("Ano:", game['ano'])

print (" ")

#Métodos para dicionários:

print(game.values()) #Informa os valores e ignora as chaves

for values in game.values(): #Iteração com valores
    print(values)
print (" ")

print(game.keys()) #Informa as palavras-chave e ignora os valores

for keys in game.keys(): #Iteração com chaves
    print(keys)
print (" ")

print(game.items()) #Informa ambos (cuidado items com 'm')

for keys, values in game.items(): #Para iteração com itens é necessário informar duas variáveis
	print (f'{keys} = {values}')
#Iterar utilizando o método "items" permite realizar print de forma mais simples