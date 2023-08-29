#Exercício rateio

quant_apt = int(input('Quantidade de apartamento: '))
valor_agua = float(input('Valor da Água: '))
valor_luz = float(input('Valor da Luz: '))

valor_pagar = (valor_agua + valor_luz) / quant_apt

print('O valor por apartamento é de: ', valor_pagar)
