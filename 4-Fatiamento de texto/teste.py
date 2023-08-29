soma = 0
for i in range(2):
    frase = input('frase:')
    qnt = frase.lower().count('a')
    soma = soma+ qnt
print('Quantidade letras (A):', soma)
    
