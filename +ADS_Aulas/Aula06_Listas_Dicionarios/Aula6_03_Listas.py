#Listas:
#Estruturas de dados dinâmicas
#Podemos alterar dados e tamanho
#Indexadas por valores numéricos inteiros
#Representadas por colchetes []

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate') #Tupla
print ('Tupla: ', mochila)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate'] #Lista
print ('Lista: ', mochila)

mochila[2] = 'Laranja' #Posso alterar um item indicando o índice e realizando uma nova atribuição
print ('Lista: ', mochila)

#Manipulação de listas:

mochila.append ('Ovos') #adiciona no final da lista
print ('Lista: ', mochila)

mochila.insert (0, 'Canivete') #insere na posição informada >>índice+dado
print ('Lista: ', mochila)

del mochila[1] #deleta o índice informado
print ('Lista: ', mochila)

mochila.remove ('Ovos') #deleta o dado informado
print ('Lista: ', mochila)

#Cópia de listas:

#mesma referência
lista_original = [5, 7, 9, 11]
lista_copiada = lista_original

print (lista_original)
print (lista_copiada)

lista_copiada[0] = 2 #altera ambas >> a cópia (atribuição) não aloca um novo espaço de memória
print (lista_original)
print (lista_copiada)

#cópia
lista_original1 = [2, 4, 6, 8]
lista_copiada1 = lista_original1[:] #a cópia aloca blocos de memória distintos [:], permitindo trabalhar com as listas separadamente

print (lista_original1)
print (lista_copiada1)

lista_copiada1[0] = 0
print (lista_original1)
print (lista_copiada1)