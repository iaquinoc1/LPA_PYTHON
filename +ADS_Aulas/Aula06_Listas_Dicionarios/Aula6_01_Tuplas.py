#Variáveis:
#Simples: armazenam somente um dado
#Compostas: armazenam um conjunto de dados

#Estrutura de dados:
#Conjunto de dados organizados de uma maneira específica na memória do programa

#Tupla: estrutura estática, imutável, representada por parênteses ()

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')

print (mochila)
print (mochila[0])
print (mochila[2])
print (mochila[0:2])
print (mochila[-1])

print (" ")

for item in mochila:
	print(f'Na minha mochila tem: {item}')

print (' ')

tam = len(mochila)
for i  in range (0, tam, 1):
	print(f'Na minha mochila tem: {mochila[i]}')

print(' ')

upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade
print('A mochila grande tem', mochila_grande)