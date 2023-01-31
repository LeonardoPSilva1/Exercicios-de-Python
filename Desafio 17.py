#para encontrar a hipotenusa o calculo é A2 = b2 + c2
from math import hypot

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('a hipotenusa vai ser de {:.2f}'.format(hi))

hi = hypot(co, ca)
print('a hipotenusa vai medir: {:.2f}'.format(hi))