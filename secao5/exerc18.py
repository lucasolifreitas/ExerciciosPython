print('1 - SOMA')
print('2 - MULTIPLICAÇÃO')
print('3 - SUBTRAÇÃO')
print(('4 - DIVISÃO'))


operador = int(input('Escolha um operador'))
num1 = float(input('Informe o primeiro numero: '))
num2 = float(input('Informe o segundo numero: '))

if operador == 1:
    print(f'A soma entre {num1} e {num2} é: {num1 + num2} ')
elif operador == 2:
    print(f'A multiplicação entre {num1} e {num2} é: {num1 * num2}')
elif operador == 3:
    print(f'A subtração entre {num1} e {num2} é: {num1 - num2}')
elif operador == 4:
    if num2 != 0:
        print(f'A divisão entre {num1} e {num2} é: {num1 / num2}')
    else:
        print('O denominador deve ser diferente de 0')
else:
    print('Operador Inválido!')
