for i in range (3):
    placa = input('Placa:')
    if placa[3].isnumeric() and placa[5:].isnumeric():
        soma =int(placa[3]) + int(placa[5]) + int(placa[6])
        print('Soma dos números:', soma)
