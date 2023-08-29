qnt = 1
soma = 0

while qnt <= 20:
    idade = int(input('Idade:'))
    soma = soma + idade
    qnt += 1
    media = soma / 20
print('Média das idades:', media)
