from datetime import date

ano_atual = date.today().year

idade = int(input('Quantos anos voce tem? '))

print(f'Você nasceu no ano de {ano_atual - idade}')
