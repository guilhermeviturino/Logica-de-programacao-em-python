#Cálculo do salário Líquido
#variáveis que serão recebidas
sal_base = float(input('Informe o Salário base: '))
vant = float(input('Informe o total das vantagens: '))
desc= float(input('Informe o total dos descontos: '))

#Processamento
sal_liq = (sal_base + vant) - desc

#Saída
print('O salário líquido calculado foi: ', sal_liq)
