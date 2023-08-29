idade = int(input('Idade:'))
if idade < 16:
    print('Não elegivél')
elif idade >= 18 and idade < 65:
    print('eleitor obrigatório')
elif idade >= 16 and idade <= 18 or idade >= 65:
    print('Eleitor facultativo')
