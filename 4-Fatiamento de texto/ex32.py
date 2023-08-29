nome = input('Nome:')

tam = len(nome)
metade = tam // 2
p1 = nome[0:metade]
p2 = nome[metade:]
senha = p2[0:2] + '%%' + p1[-3:]

print('Parte1:', p1)
print('Parte2:', p2)
print('Senha:', senha)
