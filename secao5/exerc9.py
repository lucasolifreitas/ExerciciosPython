salario = float(input('Informe o salario do funcionario: R$'))
emprestimo = float(input('Informe o valor do emprestimo: R$'))

if emprestimo > ((salario * 20)/100):
    print('Emprestimo negado, pois o valor ultrapassa 20% do seu salário!')
else:
    print('Emprestimo concedido!')


