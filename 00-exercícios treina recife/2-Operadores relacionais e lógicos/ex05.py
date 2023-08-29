'''saldo = int(input('Saldo:'))
if saldo <= 500:
    print('Nenhum saldo disponivél.')
else:
    if saldo <= 1000:
        print('30% do valor do saldo')
    else:
        if saldo <= 3000:
            print('40% do valor do saldo')
        else:
            print('50% do valor do saldo')'''


saldo = int(input('Saldo:'))
if saldo <= 500:
    print('Nenhum saldo disponivél.')
elif saldo > 500 and saldo <= 1000:
    print('30% do valor do saldo')
elif saldo > 1000 and saldo <= 3000:
    print('40% do valor do saldo')
else:
    print('50% do valor do saldo')
