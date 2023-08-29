idade = int(input('Idade:'))
if idade < 21:
    print('menor de idade')
elif idade >= 21 and idade < 65:
    print('maior de idade')
else:
    print('idoso')
