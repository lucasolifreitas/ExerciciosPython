lista = list()
for i in range(2, 51*2, 2):
    lista.append(i)
print(lista)
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(f'A soma dos 50 primeiros números pares é: {soma}')
