salario_base = float(input('Digite o salario base do funcionario: R$'))
salario_receber = (salario_base + (salario_base*5/100) - (salario_base*7/100))
print(f'O funcionario receberá {salario_receber}')
