#Exercício descontos
#desconto 1


sal_bruto = float(input('Valor total do salário: '))
vlr_ir = (sal_bruto * 5) / 100
vlr_inss = (sal_bruto * 11) / 100
sal_liq = sal_bruto - vlr_ir - vlr_inss
print('')
print('Total imposto de renda=', vlr_ir)
print('Total inss= ', vlr_inss)
print('Salário total com todos os descontos= ', sal_liq)
