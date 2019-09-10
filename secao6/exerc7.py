lista = []
for i in range(0, 10):
    num = int(input(f'Digite o valor {i +1} :'))
    while num < 0:
        print('Digite um valor maior que 0 (zero)!!')
        num = int(input(f'Digite o valor {i + 1} :'))
    lista.insert(i, num)
soma = 0
for i in range(len(lista)):
    soma += lista[i]

print(f'A media dos numeros {lista} é: {soma / len(lista)}')

