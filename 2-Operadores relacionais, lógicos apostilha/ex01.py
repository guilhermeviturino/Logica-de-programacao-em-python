peso = float(input('Peso:'))
excesso = peso - 50
multa = excesso * 4

if peso <= 50:
    print('peso ok')
if peso > 50:
    print('excesso=', excesso)
    print('multa=', multa)
