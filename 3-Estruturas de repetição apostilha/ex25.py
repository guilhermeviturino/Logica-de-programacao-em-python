pais_a = float(input('Pais A:'))
pais_b = float(input('Pais B:'))

anos = 0
porcentagem_a = 3
porcentagem_b = 1.5


while pais_a < pais_b:
    pais_a = pais_a + (pais_a * 3/100)
    pais_b = pais_b + (pais_b * 1.5/100)
    anos += 1
print('Quantidade anos:', anos,'anos')
    
