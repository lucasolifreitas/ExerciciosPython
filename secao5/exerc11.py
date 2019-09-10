num = str(input('Infome um numero: '))
soma = 0
if int(num) > 0:
    for i in range(len(num)):
        soma += int(num[i])
    print(f'A soma dos algarismos do número {num} é: {soma}')
else:
    print(f'Numero inválido!')


