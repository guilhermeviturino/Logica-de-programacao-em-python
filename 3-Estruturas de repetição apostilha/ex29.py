resp_sim = 0
resp_nao = 0
qnt_total = 0
f_sim = 0
total_m = 0
total_f = 0
m_nao = 0

while True:
    sexo = input('Digite o sexo:')
    if sexo == 'fim':
        break
    resposta = input('sim ou nao:')
    if sexo == 'f':
        total_f += 1
        if resposta == 'sim':
            f_sim += 1
        if resposta == 'nao':
            resp_nao += 1 
    elif sexo == 'm':
        if resposta == 'nao':
            m_nao += 1
    qnt_total += 1

porcentf = (f_sim * 100) / total_f 
porcentm = (m_nao * 100) / qnt_total
print('Responderam sim:', f_sim)
print('Responderam não:', m_nao)
print('Porcentagem feminina sim:', porcentf,'%')
print('Porcentagem masculina não:', porcentm,'%')
