peso = float(input('Qual é seu peso?(kg)'))
altura = float(input('Qual é a sua atura?'))
imc = peso / (altura **2)
print('O imc dessa pessoa é de:{:.1f}'.format(imc))

if imc < 20:
    print('abaixo do peso')
elif imc <= 25:
    print('Peso normal')
elif imc <= 30:
    print('Sobre peso')
elif imc <= 40:
    print('Obeso')
else:
    print('Obeso mórbido')
