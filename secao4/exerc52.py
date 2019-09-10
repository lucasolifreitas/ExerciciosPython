aposta1 = float(input('Informe o valor da primeira aposta: R$'))
aposta2 = float(input('Informe o valor da segunda aposta: R$'))
aposta3 = float(input(('Informe o valor da terceira aposta: R$')))

valor_apotas = aposta1 + aposta2 + aposta3

porcentagem1 = (aposta1)/valor_apotas
porcentagem2 = (aposta2)/valor_apotas
porcentagem3 = (aposta3)/valor_apotas

premio_total = float(input('Informe o premio total: R$'))

print(f'O primeiro amigo receberá: R${round(premio_total*porcentagem1,2)}')
print(f'O segundo amigo receberá: R${round(premio_total*porcentagem2,2)}')
print(f'O terceiro amigo receberá: R${round(premio_total*porcentagem3,2)}')