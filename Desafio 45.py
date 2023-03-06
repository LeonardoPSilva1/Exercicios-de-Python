from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)


print('''Escolha: 
[ 0 ] Tesoura 
[ 1 ] Papel
[ 2 ] Tesoura
''')

jogador = int(input('Qual a sua jogada?? '))

print('JÓOOOOOOOOOOOOOO')
sleep(1)
print('KENNNNNNNNNNNNNNNN')
sleep(1)
print('PO!')

print('-='*11)

print('Computador Jogou: {}'.format(itens[computador]))
print('Jogador Jogou: {}'.format(itens[jogador]))

print('-='*11)

if computador == 0: #jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador GANHOU!')
    elif jogador == 2:
        print('Foi de F no chat')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #jogou papel
    if jogador == 0:
        print('Foi de F no chat')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador GANHOU!')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #jogou Tesoura
    if jogador == 0:
        print('Jogador GANHOU!')
    elif jogador == 1:
        print('Foi de F no chat')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVALIDA')

