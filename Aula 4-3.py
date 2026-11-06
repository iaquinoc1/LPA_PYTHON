# x = 1
# while (x <= 48):
#     print (x)
#     x += 8
# 
# for x in range (1, 48, 8):
#     print (x)

# x = 3
# while (x <= 12):
#     print (x)
#     x += 3
# 
# for x in range (3, 13, 3):
#     print (x)
# 
# x = 0
# while (x < 9):
#     print (x)
#     x += 2
# 
# for x in range (0, 9, 2):
#     print (x)
# 
# print ('LANCHONETE')
# print ('1 - Coxinha R$ 5,00')
# print ('2 - Pastel R$ 7,00')
# print ('3 - Café R$ 4,00')
# print ('4 - Suco R$ 6,00')
# print ('5 - SAIR')
# 
# total = 0
# while True:
#     op = int(input('Qual item gostaria de comprar?'))
#     
#     if (op == 1):
#         qtd = int(input('Quantas unidades quer comprar?'))
#         total = total + qtd * 5.00
#     elif (op == 2):
#         qtd = int(input('Quantas unidades quer comprar?'))
#         total = total + qtd * 7.00
#     elif (op == 3):
#         qtd = int(input('Quantas unidades quer comprar?'))
#         total = total + qtd * 4.00
#     elif (op == 4):
#         qtd = int(input('Quantas unidades quer comprar?'))
#         total = total + qtd * 6.00
#     elif (op == 5):
#         break
#     else:
#         print ('Opção inválida')
# 
# print (f'Valor total R$ {total}')
# 
# valor = int(input('Digite o valor desejado: '))
# 
# while True:
#     if valor >= 100:
#         cont100 = valor // 100
#         valor -= cont100 * 100
#         print (f'{cont100} cédulas de 100')
#         if not valor:
#             break
#     if valor >= 50:
#         cont50 = valor // 50
#         valor -= cont50 * 50
#         print (f'{cont50} cédulas de 50')
#         if not valor:
#             break
#     if valor >= 10:
#         cont10 = valor // 10
#         valor -= cont10 * 10
#         print (f'{cont10} cédulas de 10')
#         if not valor:
#             break
#     if valor:
#         cont1 = valor
#         print (f'{cont1} cédulas de 1')
#         break
# 
total = 0
valor = 0
while True:
    idade = int(input('Qual a idade'))
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















