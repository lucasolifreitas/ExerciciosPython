lista = []
num = int(input('Digite um numero: '))

for i in range(0, num):
    lista.append(i)
print(sorted(lista, key=int, reverse=True))
print(lista)
