qnt_imp = 0
qnt_par = 0
soma = 0
qnt_n = 0


while True:
    n = int(input('N:'))
    if n == 99: break
    if n % 2 == 0:
        qnt_par += 1
    else:
        qnt_imp += 1
qnt_n += qnt_par + qnt_imp
if qnt_n != 0:
    porcent_par = qnt_par * 100 / qnt_n
    porcent_imp = qnt_imp * 100 / qnt_n
    print('Perc PAR:', porcent_par)
    print('Perc PAR:', porcent_imp)
