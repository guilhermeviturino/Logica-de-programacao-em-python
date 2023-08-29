vlr_hr = float(input('Valor por hora: '))
distancia = float(input('Distancia km: '))
duracao = int(input('Horas de show: '))

deslocamento = (50 * distancia)
vlr_show = (vlr_hr * duracao) + deslocamento
frete = (35 * deslocamento) / 100 

print('Valor do show:', vlr_show)
print('Valor do frete:',frete)
