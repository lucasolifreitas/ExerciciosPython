valor_a = 0;
while valor_a == 0:
    print('O valor de a deve ser diferente de zero!!')
    valor_a = int(input('Entre com o valor de a: '))
valor_b = int(input('Entre com o valor de b: '))
valor_c = int(input('Entre com o valor de c: '))

delta = (valor_b ** 2) - 4 * valor_a * valor_c
print(f'Valor de delta: {delta}')
def eq_segundo_grau(a,b, delta):
    resultado = []
    x1 = (-valor_b + (delta**0.5))/2*valor_a
    resultado.append(x1)
    x2 = (-valor_b - (delta**0.5))/2*valor_a
    resultado.append(x2)
    return resultado

if delta < 0:
    print('Não existe reaiz!')
elif delta == 0:
    print('Raiz única!')
    print(f'As raizes são: {eq_segundo_grau(valor_a, valor_b, delta)}')
else:
    print('Existe duas raizes!')
    print(f'As raizes são: {eq_segundo_grau(valor_a, valor_b, delta)}')

