#Instrução global: força o programa a não criar uma variável local e manipular a variável global 

def omelete():
	global ovos #Alterada a variável global, permite alterar a mesma dentro da função
	ovos = 6

ovos = 12
omelete()
print (ovos)