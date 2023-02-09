from random import randint
from time import sleep

num = randint(0,5)

print('-=-' *10)
print('Vou escolher um numero de 0 a 5, adivinha ae')
print('-=-'*10)
numero = int(input('Escolha um numero de 0 a 5: '))

print('PROCESSANDO....')
sleep(3)

if numero == num:
    print('CAGADAAAAAA')
else:
    print('tururu, tenta denovo ai :D')
print('escolhi foi o {}'.format(num))