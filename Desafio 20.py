from random import shuffle

gp1 = str(input('representante do grupo 1: '))
gp2 = str(input('Representante do grupo 2: '))
gp3 = str(input('Representante do grupo 3: '))
gp4 = str(input('Representante do grupo 4: '))

lista = [gp1, gp2, gp3, gp4]

shuffle(lista)

print('Ordem de apresentação sera: ')
print(lista)