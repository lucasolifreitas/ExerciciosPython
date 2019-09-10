lado_a = int(input('Digite o valor do lado A: '))
lado_b = int(input('Digite o valor do lado B: '))
lado_c = int(input('Digite o valor do lado C: '))

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_b + lado_b):
    if lado_a == lado_b == lado_c == lado_a:
        print('É um triangulo Equilatero')
    elif lado_a != lado_b != lado_c != lado_a:
        print('É um triangulo Escaleno')
    else:
        print('É um triangulo isosceles')
else:
    print('Nao é um triangulo')
