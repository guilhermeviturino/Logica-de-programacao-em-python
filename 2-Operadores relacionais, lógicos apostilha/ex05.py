saldo = float(input('Saldo:'))

if saldo <= 500:
    saldo = saldo * 0
    print('Valor do crédio=',saldo)
elif saldo <= 1000:
    saldo = saldo * 1.3 - saldo
    print('Valor do crédito=', saldo)
elif saldo <= 3000:
    saldo = saldo * 1.4 - saldo
    print('Valor do crédito=', saldo)
else:
    saldo = saldo * 1.5 - saldo
    print('Valor do crédito=', saldo)
