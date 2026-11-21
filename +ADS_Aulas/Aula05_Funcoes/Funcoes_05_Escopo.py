#Escopo de uma variável é a propriedade que determina onde uma variável pode ser utilizada dentro de um programa
#Variáveis podem ser criadas dentro de funções e valer apenas dentro das funções onde foram criadas
#Variáveis locais ou globais

#def omelete ():
#	ovos = 12
#omelete()
#print(ovos)
#Erro! Ovos só está definido dentro da função"

def omelete():
	print (ovos)
ovos = 12
omelete()