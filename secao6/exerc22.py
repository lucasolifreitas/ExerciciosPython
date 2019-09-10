lista = []


while True:
    num = int(input('Digite uma nota entre 10 e 20: '))
    if 10 <= num <= 20:
        lista.append(num)
    else:
        break
soma = 0
for i in range(0, len(lista)):
    soma += lista[i]
media = soma / len(lista)

print(f'A média das notas {lista} é: {media}')
