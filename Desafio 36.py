from time import sleep

Casa = float(input('Qual o Valor da casa? '))
print('-==-'*10)
salario = float(input('Qual o seu Salario? '))
print('-==-'*10)
anos = float(input('Em quantos anos de financeamento? '))
print('-==-'*10)
prestacao = Casa / (anos * 12)

minimo = salario * 30 / 100

print('Calculando...')
sleep(5)

print('Para pagar a casa de {:.3f} em {:.0f} anos'.format(Casa, anos), end='')
print(' a prestação da casa sera de {}'.format(prestacao))

if prestacao <= minimo:
    print('Tudo ok, Emprestimo concedido')
else:
    print('Emprestimo NEGADO!')


