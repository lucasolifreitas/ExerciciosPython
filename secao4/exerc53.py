comprimento = float(input('O comprimento do terreno: '))
largura = float(input('A largura do terreno: '))

preco_tela = float(input('Preço m2 de tela: '))

area = comprimento * largura
print(area)
print(f'Para cobrir todo o terreno será gasto R$ {area * preco_tela} de tela')
