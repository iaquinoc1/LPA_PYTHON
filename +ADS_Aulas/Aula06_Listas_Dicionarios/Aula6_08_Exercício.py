#Criando listas vazias (ATENÇÃO >> muda () ou [])
#Também serve pra tuplas ou dicionários

item = list() #Esta é uma forma de criar uma lista vazia
mercado = [] #Esta é outra forma de criar uma lista vazia 

#Estrutura POO >> variavel.funcao(parametro) ou objeto.metodo(parametro) (com input)

for i in range(3): #Laço vai até 3 >> 3 itens
#Este bloco de código insere informações na primeira lista (item)
    item.append(input('Digite o nome do item:')) #Primeiro append para o nome do item
    item.append(int(input('Digite a quantidade:'))) #Segundo append para quantidade
    item.append(float(input('Digite o valor:'))) #Terceiro append para o valor
#Este código copia os valores que vão sendo inseridos na primeira lista para a segunda (mercado)
    mercado.append(item[:])
    item.clear() #clear = Metodo pra limpar lista para cadastrar próximo item
print(mercado)

#Outra solução, mais simples, com uma lista só:

mercado = []

for i in range (3): #laço com três repetições
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade: '))
    preco = float(input('Digite o valor: '))
    mercado.append([nome, qtd, preco]) #um único append, insere os três valores na lista
print(mercado)

print(' ')

soma = 0
print('Lista de compras:')
print('-' * 20)
print('item | quant | valor | total')
for item in mercado:
    #Usando indexação pra listar itens, quantidades e calcular totais
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')