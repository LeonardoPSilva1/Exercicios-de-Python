salario = float(input('Digite seu salario: '))
aumento = salario * 10 / 100
aumento2 = salario * 15 / 100
final1 = salario + aumento
final2 = salario + aumento2

if salario >= 1250:
    print('Aumento de {}'.format(aumento))
    print('Seu salario agora com os 10% é de {}R$'.format(final1))
else:
    print('Aumento de {}'.format(aumento2))
    print('Seu salario agora com os 15% é de {}R$'.format(final2))