num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

pares = []
impares = []

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

for i in range(menor, maior+1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

soma = 0
for i in range(0, len(pares)):
    soma += pares[i]

multiplicacao = 1
for i in range(0, len(impares)):
    multiplicacao *= impares[i]

print(f'A soma dos números pares: {pares} é: {soma}')
print(f'A multiplicação dos números ímpares: {impares} é: {multiplicacao}')

