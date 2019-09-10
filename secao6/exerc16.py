num = int(input('Infome o valor de N: '))
lista = []

for i in range(1,num,2):
    lista.append(i)
print(sorted(lista, reverse=True))

