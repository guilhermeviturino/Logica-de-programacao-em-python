qnt = 1
maior = 0

while True:
    idade = int(input('Idade:'))
    if idade == 100:
        break
    if idade > maior:
        maior = idade
print('A maior idade:', maior)
