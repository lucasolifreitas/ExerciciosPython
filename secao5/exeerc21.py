print('Escolha a opção: ')
print('1 - Soma de 2 números')
print('2 - Diferença entre 2 números (maior pelo menor')
print('3 - Produto entre 2 numeros')
print('4 - Divisão entre 2 nuemros ( o deniminador nao pode ser zero)')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print(f'A soma entre {num1} e {num2} é: {num1 + num2}')
elif opcao == 2:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    if num1 > num2:
        maior = num1
        menor = num2

    else:
        maior = num2
        menor = num1
    print(f'A digerença entre {maior} e {menor} é: {maior - menor}')
elif opcao == 3:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print(f'O produto entre {num1} e {num2} é: {num1 * num2}')
elif opcao == 4:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    if num2!=0:
        print(f'A divisão entre {num1} e {num2} é: {num1 / num2}')
    else:
        print('Denominador deve ser maior que zero!!')
else:
    print('Opção inválida!!')