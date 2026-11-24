#É possível acessar o índice de strings dentro de listas. 
#Indexação dupla - por item e por caractere.
#O primeiro índice é ref. ao item da lista, o segundo ao caracteres da string.

mercado = [['Cebola', 0.39], ['Tomate', 0.47], ['Maçã', 0.85]]

print (mercado [2][1]) #Índice 2 (terceiro item), índice 1 (segundo item)
print (mercado [0][0][0:3]) #Índice 0 (primeiro item), índice 0 (primeiro termo), índice 0:3 (caracteres 1 a 3)
print (mercado [2][1][0]) #NÃO FUNCIONA COM INT OU FLOAT (somente string)