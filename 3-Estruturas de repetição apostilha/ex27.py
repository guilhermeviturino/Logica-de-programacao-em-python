qnt = 0
soma = 0
maior = 0
qntf = 0

while True: 
    sexo = input('Sexo:')
    if sexo == 'fim':
        break
    altura = float(input('Altura:'))
    if sexo == 'm':
        qnt = qnt + 1
        if altura > maior:
            maior = altura
    else:
        if sexo == 'f':
            soma = soma + altura
            qntf = qntf + 1
            media = soma / qntf
            if altura > maior:
                maior = altura

print('Maior altura:', maior)
print('Média altura f:', media)
print('Qntd homens:', qnt)
