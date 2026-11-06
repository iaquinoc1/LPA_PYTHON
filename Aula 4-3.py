total = 0
valor = 0
while True:
    idade = int(input('Qual a idade: '))
    if idade == 0:
        break
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    valor += ingresso

if total > 0:
    print (f'Ingressos: {total}')
    print (f'Valor: {valor}')        

