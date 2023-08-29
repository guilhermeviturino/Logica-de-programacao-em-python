cont = 1
maior = -1
menor = 999
soma = 0
qnt = 0
while cont <= 2:
    nome = input('Nome:')
    idade = int(input('Idade:'))
    qnt += 1
    soma += idade
    if idade > maior:
        maior = idade
        
    if idade < menor:
        menor = idade
        nome_nova = nome
    cont += 1
media = soma  / qnt 
print('Maior idade:', maior)
print('Pessoa mais nova:', nome_nova)
print('Media das idades:', media)
