def valida (pergunta, min, max):
	s1 = input(pergunta)
	tam = len (s1)
	while ((tam < min) or (tam > max)):
		s1 = input(pergunta)
		tam = len(s1)
	return s1
x = valida ('Digite uma string:', 10, 30)
print ('Você digitou a string: {}. \n Dado válido. Encerrando o programa...' .format(x))