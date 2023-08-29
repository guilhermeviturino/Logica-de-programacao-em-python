n = int(input('N:'))
dm = n // 10000
r1 = n % 10000
m = r1 // 1000
r2 = r1 % 1000
c= r2 // 100
r3 = r2 % 100
d = r3 // 10
u = r3 % 10

if dm == u and m == d:
    print('è um palíndromo')
else:
    print('Não é um palíndromo')


