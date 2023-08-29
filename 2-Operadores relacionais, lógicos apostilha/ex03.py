salario = float(input('Salário:'))

if salario <=1100:
    salario = salario * 1.1
    print('Novo salário=', salario)
elif salario <= 2000:
    salario = salario * 1.07
    print('Novo salário=', salario)
else:
    salario = salario * 1.05
    print('Novo slário=', salario)
