while True:
    matricula = int(input('Matricula:'))
    if matricula == 99:
        break
    salario = float(input('Salario:'))
    vendas = float(input('Valor em vendas:'))
    mat = matricula
    if vendas <= 1000:
        comissao = vendas * 0.03
    else:
        diferenca = vendas - 1000
        comissao = (1000 * 0.03) + (diferenca * 0.05) 
    salario_total = salario + comissao
    print('Matrícula:', mat)
    print('Vendas:', vendas)
    print('Salário fixo:', salario)
    print('Salário total:', salario_total)
    print('')
