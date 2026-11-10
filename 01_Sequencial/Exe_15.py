area = int(input("Informe a área a ser pintada, em m2: "))

litros = area / 3
latas = litros % 18

print (f'O número de latas necessárias será de: {latas: .2f}')