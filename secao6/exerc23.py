num = int(input('Digite um número: '))

divisores = []

for i in range(1, num+1):
    if num % i == 0:
        divisores.append(i)
print(f'Os divisores de {num} são: {divisores}')
