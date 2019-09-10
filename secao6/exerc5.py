lista = []
for i in range(1, 11):
    lista.append(int(input(f'Digite o valor {i} :')))

i = 0
soma = 0
while i < len(lista):
    soma += lista[i]
    i += 1
print(f'A Soma dos numeros {lista} é: {soma}')


