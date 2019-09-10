distancia = float(input('Informe a distancia: '))
litros_consumidos = float(input('Informe a quantidade de combustível gasto no percurso: '))

km_l = distancia / litros_consumidos

if km_l < 8:
    print(f'km/l: {km_l}. Venda o carro!')
elif 8 <= km_l < 14:
    print(f'km/l: {km_l}. Econômico!')
elif km_l > 12:
    print(f'km/l: {km_l}. Super Econômico!')
