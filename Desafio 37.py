n1 = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases: 
[ 1 ] Converter para Binario:
[ 2 ] Converter para octal:
[ 3 ] Converter para Hexadecimal''')

opção = int(input('Escolha uma das 3 opções: '))
if opção == 1:
    print('{} Convertido para binario é {} '.format(n1, bin(n1)[2:]))
elif opção == 2:
    print('{} convertido para octal {} '.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('{} Convertido para Hexadecimal {} '.format(n1, hex(n1)[2:]))
else:
    print('Opção invalida')

