while True:
    valorsaque = int(input('Valor:'))
    if valorsaque == -1:
        break
    qnt_50 = valorsaque // 50
    r1 = valorsaque % 50
    qnt_20 = r1 //20
    r2 = r1 % 20
    qnt_10 = r2 // 10
    qnt_1 = r2 % 10
    print('R$ 50,00 -', qnt_50)
    print('R$ 20,00 -', qnt_20)
    print('R$ 10,00 -', qnt_10)
    print('R$ 1,00 -', qnt_1)
    
