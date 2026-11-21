#Parâmetros: dados recebidos pelas funções
#Passagem de parâmetros: ato  de enviar um dado para uma função

def realce (s1):
	print ('|', '_' * 10, '|')
	print ('|', '_' * 10, '|')
	print ('   ', s1)
	print ('|', '_' * 10, '|')
	print ('|', '_' * 10, '|')
s1 = input("Digite uma palavra: ")
realce (s1)