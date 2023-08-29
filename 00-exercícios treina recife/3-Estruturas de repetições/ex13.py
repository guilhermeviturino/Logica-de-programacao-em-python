qnt = 1
maior = -1
menor = 999
soma = 0
qnt_f = 1
qnt_m = 0

while qnt <= 3:
    sexo = input('Sexo:')
    altura = float(input('Altura:'))
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura
    qnt += 1
    
    if sexo == 'f':
        soma += altura
        media = soma / qnt_f
        qnt_f += 1
    else:
        qnt_m += 1
print('Maior altura:', maior)
print( 'Menor altura:', menor)
print('Média das alturas f:', media)
print('Número de homens:', qnt_m)
