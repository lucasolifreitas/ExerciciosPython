hora_inicio = int(input('Digite a hora de inicio: '))
minuto_inicio = int(input('Digite o minuto de inicio: '))
segundo_inicio = int(input('Digite o segundo de inicio: '))

duracao = int(input('Informe a duraçao em segundos: '))

hora_final = int(duracao / 3600)
valor = duracao - (hora_final*3600)
minuto_final = int(valor / 60)
segundos_final = valor - (minuto_final*60)

print(f'A experiencia deve terminar as {hora_final + hora_inicio}h{minuto_final+minuto_inicio}min{segundo_inicio+segundos_final}')
