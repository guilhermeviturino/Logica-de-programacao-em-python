qnt = 1
qnt_dentro = 0
qnt_fora = 0

while qnt <= 4:
    valor = int(input('Valor:'))
    if valor >= 10 and valor <= 20:
        qnt_dentro += 1
    else:
        qnt_fora += 1
    qnt += 1
print('Quantidade dentro do intervalo:', qnt_dentro)
print('Quantidade fora do intervalo:', qnt_fora)


