valor_produto = float(input('Informe o valor do produto: '))
estado = str(input('Informe o estado: ')).upper()

if estado == 'MG':
    preco = valor_produto + (valor_produto*(7/100))
    print(f'O preço do produto será de {preco}')
elif estado == 'SP':
    preco = valor_produto + (valor_produto*(12/100))
    print(f'O preço do produto será de {preco}')
elif estado == 'RJ':
    preco = valor_produto + (valor_produto*(15/100))
    print(f'O preço do produto será de {preco}')
elif estado == 'MS':
    preco = valor_produto + (valor_produto*(8/100))
    print(f'O preço do produto será de {preco}')
else:
    print('Estado inválido!')
