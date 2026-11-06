v1 = int(input('Digite o valor 1: '))
oper = input('Operação')
v2 = int(input('Digite o valor 2: '))

if oper == '+':
  res = v1 + v2
  print (res)
elif oper == '-':
  res = v1 + v2
  print (res)
elif oper == '*':
  res = v1 * v2
  print (res)
elif oper == '/':
  res = v1 / v2
  print (res)
elif oper == '+' or '-' or '*' or '/':
  print('Erro')