i = 0
lista = []
lista2 = []

while i < 5:
    lista.append(int(input(f'Digite o {i+1}º numero: ')))
    lista2.append((lista[i])**2)
    i = i+1
print(lista)
print(lista2)

