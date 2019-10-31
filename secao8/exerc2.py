"""
Faça uma função que receba a data atual ( dia, mês  e ano em inteiro ) e exiba-a na tela
no formato textual por extenso. Exemplo: data: 01/01/2000, imprimir: 1 de janeiro de 2000
"""
import datetime
from textblob import TextBlob

#precisa de conexão de internet!!!!
def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()


def data(data):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    if data[3] == 0:
        mes = meses[int(data[4]) - 1]
    else:
        mes = meses[int(data[3:5]) - 1]

    return f'{data[0:2]} de {mes} de {data[6:10]}'



print(data('01/12/1992'))