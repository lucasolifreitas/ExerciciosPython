print('AREA DO TRAPÉZIO')
print('')

base_menor = float(input('Informe a base menor: '))
base_maior = float(input('Informe a base maior: '))
altura = float(input('Informe a altura: '))

if base_maior > 0 and base_menor >0 and altura >0:
    area = ((base_menor + base_maior) * altura)/2
    print(f'A área do Trapézio é: {area}')
else:
    print('Parâmetros inválidos')

