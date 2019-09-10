num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print(f'{num1} e {num2} são iguais!')

