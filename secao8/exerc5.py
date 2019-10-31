"""
Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
V = 4/3 * pi * R³
"""
import math


def volume_esfera(raio):
    v = (4/3) * math.pi * (math.pow(raio, 3))
    return round(v, 4)

print(volume_esfera(3))