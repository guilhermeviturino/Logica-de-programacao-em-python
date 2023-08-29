idade = -1
qntf = 0
f_verde = 0
soma = 0
while True:
    sexo = input('Sexo: Digite m ou f   ')
    if sexo == 'fim':
        break
    cor_olhos = input('Cor dos olhos: Digite v (erde) ou a (zul)   ')
    anos = int(input('Idade:'))
    if anos > idade:
        idade = anos
        
    if sexo == 'f':
        qntf +=1
        if cor_olhos == 'v' and anos >= 18 and anos <= 35:
            f_verde += 1
print('A maior idade dos habitantes:', idade)
porcent = (f_verde*100) / qntf
print('Porcentagem Fem cujo idade 18 a 35 anos e olhos verde:', porcent)

    
