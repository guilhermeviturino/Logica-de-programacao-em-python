qnt = 1
soma = 0
while True:
    idade = int(input('Idade:'))
    if idade == 0:
        break
    soma += idade
    media = soma / qnt
    qnt += 1
print('Média das idades:', media)
