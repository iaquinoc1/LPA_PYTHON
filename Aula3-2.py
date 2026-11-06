idade = int(input('Digite sua idade: '))
if idade > 60:
  print ('Você tem direito ao benefício.')
else:
  print('Você não tem direito ao benefício.')


dano = int(input('Digite o valor do dano: '))
escudo = int(input('Digite o valor do escudo: '))
if dano > 10 and escudo == 0:
  print ('Você está morto.')
else:
  print ('Você escapou.')

norte = True
sul = False
leste = False
oeste = True

if (norte == True or sul == True or leste == True or oeste == True):
  print ("Você está vivo")