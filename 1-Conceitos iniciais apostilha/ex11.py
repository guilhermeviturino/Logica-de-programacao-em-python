duracao_segundos = int(input('Digite o tempo de duração em segundos :'))

horas = duracao_segundos // 3600
minutos = duracao_segundos % 3600 // 60
segundos = duracao_segundos % 60

#print(f'A duração do evento é de: {horas} horas, {minutos} minutos e {segundos} segundos.')
print(str(horas).rjust(2,'0')+':'+str(minutos).rjust(2,'0')+':'+str(segundos).rjust(2,'0'))
