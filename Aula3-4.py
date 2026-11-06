lado1 = int(input("Digite o valor do segmento A-B: "))
lado2 = int(input("Digite o valor do segmento B-C: "))
lado3 = int(input("Digite o valor do segmento A-C: "))

if (lado1 > 0 and lado2 > 0 and lado3 > 0) and (lado1+lado2 > lado3 and lado2+lado3 > lado1 and lado1+lado3 > lado2):
#Se chegou até aqui é porque o triângulo é válido!
  if lado1 == lado2 == lado3:
    print ('Triângulo equilátero')
  elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
    print ('Triângulo isósceles')
  elif lado1 != lado2 != lado3:
    print ('Triângulo escaleno')
else:
  print ("Não é um triângulo!")