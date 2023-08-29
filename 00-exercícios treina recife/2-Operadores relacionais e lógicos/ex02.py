from num2words import num2words
n = int(input('Valor:'))
print(num2words(n, lang='pt-br'))
print(num2words(n, lang='pt-br', to='ordinal'))
