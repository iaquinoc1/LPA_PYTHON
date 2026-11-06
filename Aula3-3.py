ano = int(input("Digite o ano:"))
if ano%4 == 0:
  print ("Pode ser um ano bissexto")
else:
  print ("Não é um ano bissexto")

cima = True
baixo = True
if cima == True and baixo == False:
  print ("Decida-se!")
else:
  print ("Você escolheu um caminho!")