rh = float(input('RH:'))
rm = float(input('RM:'))
rc = rh + rm

if rc <= 900:
    porcentagem =0
elif rc <= 1500.00:
    porcentagem = 10
elif rc <= 2500.00:
    porcentagem = 15
else:
    porcentagem = 25

ir = (rc * porcentagem) / 100 
renda_liquida = rc - ir
print('Valor renda conjunta=', rc)
print('Vlr_aliq=', porcentagem)
print('Valor IR=', ir)
print('Renda liquida=', renda_liquida)

                
