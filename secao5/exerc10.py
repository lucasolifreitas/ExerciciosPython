altura = float(input('Informe sua altura: '))
sexo = ''
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Informe seu sexo: (M/F): ')).upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal}')
if sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal}')
