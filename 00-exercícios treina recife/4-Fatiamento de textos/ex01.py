qnt = 0
for i in range(5):
    frase = input('frase:')
    qnt = qnt + frase.lower().count('a')
print('Quantidade letras (A):', qnt)
    
