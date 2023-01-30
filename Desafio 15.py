km = int(input('Quantos km rodados: '))
dia = int(input('quantos dias foi alugado: '))

kmr = km * 0.15
dias = dia * 60

total = dias + kmr

print('km rodados: {}'.format(km))
print('voce ficou com o carro por: {}'.format(dia))
print('total para pagar os km: {}'.format(kmr))
print('total a ser pago pelos dias: {}'.format(dias))

print('total a pagar é exatamente: {}'.format(total))
