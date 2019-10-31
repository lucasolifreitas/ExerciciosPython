"""
Faça uma função para verificar se um número é quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que pode ser expresso como quadrado
de outro número inteiro.
"""

def quadrado_perfeito(num):
    if num > 0 and type(num) == int:
        return num ** 2
    else:
        return  'O número deve ser inteiro positivo!'

print(quadrado_perfeito(9))
