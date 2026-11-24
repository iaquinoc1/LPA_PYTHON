#É possível acessar o índice de strings dentro de listas. 
#Indexação dupla - por item e por caractere.
#O primeiro índice é ref. ao item da lista, o segundo ao caracteres da string.

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate'] #Lista
print(mochila [0][0])
print(mochila[2][3])

print (" ")

for item in mochila:
	for letra in item:
		print (letra, end="")
	print()

print (" ")

for i in range (0, len(mochila), 1):
	for j in range (0, (len(mochila[i])), 1):
		print(mochila[i][j], end="")
	print()

print ('')

