valor = float(input('Digite o valor: R$'))
total_desconto_dez = valor - (valor*10/100)
parcela = valor / 3
comissao_vista = total_desconto_dez * 5/100
comissao_prazo = valor * 5/100

print(f'O total a pagar com 10% de desconto será: R${total_desconto_dez}')
print(f'O valor de cada parcela do produto dividio em 3x será de: R${parcela}')
print(f'A comissão do vencedor se vender a vista será de: R${comissao_vista}')
print(f'A comissao do vencedor se vender a prazo seá de: R${comissao_prazo}')
