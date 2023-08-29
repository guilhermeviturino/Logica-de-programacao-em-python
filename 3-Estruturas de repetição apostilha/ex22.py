qnt = 0
soma = 0
qnt_par = 0
soma_par = 0

while True:
    n= float(input('Número:'))
    if n == 999:
        break
    qnt += 1
    soma = soma + n
    resto = n % 2
    if resto == 0:
        soma_par += n
        qnt_par += 1

if qnt_par != 0:
    media_par = soma_par / qnt_par
else:
    media_par = 0
    
print('Quantidade:', qnt)
print('Soma:', soma)
print('Media dos pares:', media_par)  
