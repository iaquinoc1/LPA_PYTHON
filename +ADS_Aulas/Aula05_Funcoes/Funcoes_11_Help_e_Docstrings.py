#Docstrings >> strings inseridas dentro do código que explicam seu funcionamento
#Inicia com aspas triplas e encerra com aspas triplas; utilizar para funções
#Help >> função que permite acessar parâmetros de funções

def soma3 (x = 0, y = 0, z = 0):
	'''
	Explicação do funcionamento da função:
	:param x: número inteiro, opcional
	:param y: número inteiro, opcional
	:param z: número inteiro, opcional
	'''
	return x + y + z
print (soma3 (3, 2, 99))
help(soma3)
help(print)
