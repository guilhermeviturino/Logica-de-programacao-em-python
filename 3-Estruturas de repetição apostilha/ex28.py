qnt_termo = int(input('Termo:'))
a = 1
print(a)
b = 1
print(b)
termo = 2
while termo < qnt_termo:
    c = a + b
    print(c)
    a = b
    b = c
    termo += 1
