num = int(input('Digite um numero: '))

soma = 0
for i in range(1, num):
    if num % i == 0:
        soma += i
print(soma)