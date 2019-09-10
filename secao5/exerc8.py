nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota:'))

if (0 <= nota1 <= 10) and (0 <= nota2 <= 10):
    media = (nota2 + nota1)/2
    print(f'A média do aluno é: {media}')
else:
    print('Por favor, digite uma nota válida ( acima de 0 e menor de 10)')

