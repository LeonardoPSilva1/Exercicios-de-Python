# algoritno para ler o preço e dar um novo preço com 5% de desconto

prod = float(input('Preço do produto: '))
soma = prod * 0.05
desc = prod - soma

print('O produto custa: {}R$, com o desconto de 5%: {}R$, ficara com o preço novo de {}R$'.format(prod, soma, desc))