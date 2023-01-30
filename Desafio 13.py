#leia o salario de um funcionario e de a ele um aumento de 15%

salario = float(input('Digite seu salario aqui: '))
aumento = salario * 15 / 100
final = salario + aumento

print('aumento: {}R$'.format(aumento))
print('salario final de: {}'.format(final))