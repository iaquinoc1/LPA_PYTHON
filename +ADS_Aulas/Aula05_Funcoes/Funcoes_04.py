def borda (s1):
	tam = len (s1) #só imprime caso exista algum caractere
	if tam:
		print ('+', '-' * tam, '+')
		print ('|', s1, '|')
		print ('+', '-' * tam, '+')
s1 = input("Digite uma palavra: ")
borda (s1)
