lista = []
i = 0
num = 0
while i < 6:
    num = input(f'Digite o {i + 1}º número: ')
    while not num.isdigit():
        print('Por favor, digite um número!!')
        num = input(f'Digite o {i + 1}º número: ')
    lista.append(num)
    i += 1

print(lista)
lista.reverse()
print(lista)
