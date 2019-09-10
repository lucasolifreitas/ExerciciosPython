laboratorio = float(input('Informe a nota do trabalho no laboratorio: '))
exame_semestral = float(input('Informe a nota do exame semestral: '))
exame_final = float(input('Informe a nota do exame final: '))

media = (exame_final * 0.5) + (exame_semestral * 0.3) + (laboratorio * 0.2)

if media < 3:
    print(f'Sua média foi {media}, logo voce esta REPROVADO!')
elif 3 <= media < 5:
    print(f'Sua média foi {media}, logo voce esta em RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media}, logo voce esta APROVADO!')
