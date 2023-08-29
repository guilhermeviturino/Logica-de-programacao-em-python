soma = 0
qnt = 1
maiorpar = -1
qnt_imp = 1
maior = -1
menor = 999

while qnt <= 5:
    n = int(input('N:'))
    if n % 2 != 0:
        soma += n
        media = soma / qnt_imp
        qnt_imp += 1
    
    if n > maior:
        maior = n
    else:
        if n < menor:
            menor = n
            
    if n % 2 == 0:
        if n > maiorpar:
            maiorpar = n
    if n > maior:
        maior = n
    else:
        if n < menor:
            menor = n
    diferenca = maior - menor
    qnt += 1
print('Media números ímpares:',media)
print('Maior número par:',maiorpar)
print('Diferença do maior número pro menor:',diferenca)
