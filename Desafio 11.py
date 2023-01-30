#leia largura e altura e calcule sua area

l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
are = l * a


print('o calcula da largura: {}m X altura: {}m é: {}m2'.format(l, a, are))

tin = are / 2

print('para pintar a parede precisa de {:.3f}l de tinta'.format(tin))