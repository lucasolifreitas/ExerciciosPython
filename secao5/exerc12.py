import math

num = int(input('Informe o número: '))
if num > 0:
    print(f'O log na base 10 de {num} é: {math.log10(num)}')
else:
    print('Número inválido!!')

