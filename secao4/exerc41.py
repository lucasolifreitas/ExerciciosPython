valor_hora = float(input('Digite o valor da hora trabalha: '))
horas_trabalhas = float(input('Digite quantas horas o funcionario trabalhou: '))
salario = (valor_hora * horas_trabalhas) + ((valor_hora * horas_trabalhas) * 10/100)
print(f'O funcionario receberá {salario}')
