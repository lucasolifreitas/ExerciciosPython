lista = []
menor = 0
maior = 0

for i in range(0, 10):
    num = int(input(f'Digite o numero {i + 1}: '))
    if i == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor  = num
        elif num > maior:
            maior = num
    lista.insert(i, num)
print(f'O maior é: {maior}')
print(f'O menor é: {menor}')

