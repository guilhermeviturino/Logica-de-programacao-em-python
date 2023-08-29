#Exrcício 08

nome =(input('Digite seu nome: '))
salario = float(input('Digite seu salário: '))
vendas = float(input('Total em vendas :'))
receber = (vendas * 15 / 100) + salario

print('')

print('Nome :', nome)
print('Salário :', salario)
print('Total em vendas  :', vendas)
print('Valor total salário + comisão: ', receber)
