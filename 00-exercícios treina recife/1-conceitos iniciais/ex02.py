#Exercício 02

var_a = float(input('Var a: '))
var_b = float(input('Var b: '))

temp = var_a
var_a = var_b
var_b = temp

print('Os novos valores de A e B são: ')
print('Var a: ',var_a)
print('Var b: ',var_b)
