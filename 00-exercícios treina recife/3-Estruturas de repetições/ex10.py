
while True:
    n = int(input('N:'))
    if n == 0:
        break
    sub = n + 1
    soma = 0
    for volta in range (3):
        soma = soma + sub
        sub = sub + 1
    print('Soma dos subsequentes:', soma)
    media = soma / 3
    print('Média dos subsequentes', media)
