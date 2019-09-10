num = int(input('Informe um numero: '))

if (num % 3 == 0) and (num % 5 != 0):
    print(f'{num} é divisivel por 3')
if (num % 5 == 0) and (num % 3 != 0):
    print(f'{num} é divisel por 5')
