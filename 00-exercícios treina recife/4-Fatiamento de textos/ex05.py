while True:
    frase = input('Frase:')
    if frase.lower() == 'fim': break
    nfrase = frase.replace(' ', '')
    if nfrase == nfrase[::-1]:
        print('É um palíndromo')
    else:
        print('Não é um palídromo')
