qnt = 1
menor = 999

while  True :
    peso = float(input('Peso:'))
    if peso == 201:
        break
    if peso < menor:
        menor = peso
print('Menor peso=',menor)


