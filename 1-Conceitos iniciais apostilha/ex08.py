#Exercício 08
print('')
homens = float(input('Total de homens :'))
mulheres = float(input('Total de mulheress :'))
ausentes = float(input('Total ausentes :'))

presentes = homens + mulheres
total = homens + mulheres + ausentes
p1 = homens * 100 / total
p2 = ausentes * 100 / presentes
print('')
print('p1 =', p1)
print('p2 =', p2)
