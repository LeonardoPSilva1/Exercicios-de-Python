from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que voce deseja: '))

seno = sin(radians(angulo))
print('angulo {} tem o seno de {:.2f}'.format(angulo, seno))

cosseno = cos(radians(angulo))
print('angulo {} tem o cosseno de {:.2f}'.format(angulo, cosseno))

tangente = tan(radians(angulo))
print('angulo {} tem a tangente de {:.2f}'.format(angulo, tangente))

