salario = float(input('Valor do salário: '))
quant_quilowatt = float(input('Quilowatt consumido: '))
valor_quilowatt = float(1.043)
valor_conta = quant_quilowatt * valor_quilowatt
desconto = valor_conta - (valor_conta * 15) / 100 
print('')
print('Valor quilowatt: ', valor_quilowatt)
print(f'Valor da conta {valor_conta:.2f}')
print(f'Valor com desconto: {desconto:.2f}')
