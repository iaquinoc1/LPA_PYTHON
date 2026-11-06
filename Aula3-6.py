kwh = float(input('Quantos kwh: '))
tipo = input("Qual tipo de instalação? (R, C ou I)")

if tipo == 'r':
  if kwh >= 500:
    preco = 0.65
  else:
    preco = 0.4
  print (f'Total a pagar: {kwh * preco}')

if tipo == 'c':
  if kwh >= 1000:
    preco = 0.6
  else:
    preco = 0.55
  print (f'Total a pagar: {kwh * preco}')

if tipo == 'i':
  if kwh >= 5000:
    preco = 0.6
  else:
    preco = 0.55
  print (f'Total a pagar: {kwh * preco}')

else:
  print("Inválido.")