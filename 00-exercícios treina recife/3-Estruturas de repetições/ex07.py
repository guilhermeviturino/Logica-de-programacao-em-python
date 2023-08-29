boi_mais_gordo = -1
boi_mais_magro = 99999

for cont in range(3):
    n = int(input('N:'))
    peso = int(input('Peso:'))
    if peso > boi_mais_gordo:
        boi_mais_gordo = peso
        n_boi_maisgordo = n
    if peso < boi_mais_magro:
        boi_mais_magro = peso
        n_boimaismagro = n
            
print('Boi mais gordo:', boi_mais_gordo,'kg', ',','Número:', n_boi_maisgordo)
print('Boi mais magro:', boi_mais_magro,'kg',',','Número:', n_boimaismagro)
