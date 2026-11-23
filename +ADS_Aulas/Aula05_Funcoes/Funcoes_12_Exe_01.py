def fatorial(num):
    '''
    Função que calcula o fatorial de um número inteiro
    :param num: número inteiro igual ou maior que 0
    '''
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat


def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            else:
                print(f'Digite um número entre {min} e {max}.')
        except ValueError:
            print('Valor inválido. Digite apenas números inteiros.')


x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)

print(f'{x}! = {fatorial(x)}')
help(fatorial)