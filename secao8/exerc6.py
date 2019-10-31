"""
Faça uma função que receba 3 números inteiros como parâmetros,
representando horas, minutos e segundos, e os converta em segundos.
"""


def converte_segundos(hora, minuto, segundo):
    hora_segundos = hora * 3600
    minuto_segundos = minuto * 60

    return hora_segundos + minuto_segundos + segundo

print(converte_segundos(2, 45, 0))
