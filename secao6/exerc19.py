num = int(input('Informe um número entre 100 e 999: '))

while num < 100 or num > 999:
    print('Digite um número entre 100 e 999!')
    num = int(input('Informe um número entre 100 e 999: '))
str = str(num)
for i in range(0, len(str)):
    print(f'O {i+1}° algarismo do número {num} é: {str[i]}')
