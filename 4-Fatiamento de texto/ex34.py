maior = -1
for cont in range(5):
    frase = input('Frase:')
    tam = len(frase)
    if tam > maior:
        maior = tam
        maior_frase = frase
print('Maior frase:', maior_frase)
