"""
Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro
"""

def dobro(num):
    if type(num) == int:
        return num * 2
    else:
        return ('O parâmetro de entrada deve ser um número inteiro!')


