menor = 999
soma = 0
contador = 1
qntm = 0

while contador <= 3: 
    sexo = input('Sexo:')
    altura = float(input('Altura:'))
    if sexo == 'f':
        if altura < menor:  
            menor = altura
    else: 
        if sexo == 'm':
            soma = soma + altura
            qntm = qntm + 1
            media = soma / qntm     
            if altura < menor:
                menor = altura
    contador = contador + 1
print('Menor altura:', menor)
print('Media altura M:', media)


