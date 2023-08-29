qnt = 1
soma = 0

while qnt <= 5:
    n = int(input('N:'))
    soma = soma + n
    qnt = qnt + 1
    media = soma / 5
print(soma)
print(media)

for qnt in range (1,6,1):
    n = int(input('N:'))
    soma = soma + n
    media = soma / 5
print(soma)
print(media)
