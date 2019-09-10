nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = ((nota1 * 0.25) + (nota2 * 0.25) + (nota3 * 0.5))

if media >= 60:
    print(f'Sua média foi {media}, logo o aluno esta APROVADO!')
else:
    print(f'Sua média foi {media}, logo o aluno esta REPROVADO')
