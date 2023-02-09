numero = int(input('Digite um numero para ver se é impar ou par: '))
resto = numero % 2

if resto == 1:
    print('O numero {} é impar'.format(numero))
else:
    print('O numero {} é par'.format(numero))