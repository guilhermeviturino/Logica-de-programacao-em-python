

for i in range (3):
    fone = input('Fone:')
    novo_fone = fone[0:3]+'.'+fone[0:3] +'9'+ fone[0:6]+'-'+fone[7:]
    print('Fone:', novo_fone)
