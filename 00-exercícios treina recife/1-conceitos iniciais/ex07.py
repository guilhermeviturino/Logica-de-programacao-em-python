#Exercício 07

preco_custo = float(input('Preço de custo do produto: '))
porcentagem = float(input('Informe um percentual: '))
valor_venda = (preco_custo * porcentagem / 100) + preco_custo

print('Valor de venda de acordo com percentual informado :', valor_venda)
