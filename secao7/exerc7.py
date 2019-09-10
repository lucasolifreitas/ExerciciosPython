lista = []
i = 0
maior = 0
posicao = 0
while i < 10:
    num = (int(input(f'Digite o {i + 1}º número: ')))
    lista.append(num)
    if num > maior:
        maior = num
        posicao = i
    i = i +1


print(f'Os números inseridos são: {lista}')
print(f'O maior elemento inserido é: {maior}')
print(f'Ele se encontra na posição: {posicao}')


