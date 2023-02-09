from random import randint

v = randint(50,100)
r = 80


print('Voce esta a {} Km/h'.format(v))
if v >= r:
    multa = (v-r)  * 7
    print('Olha a multa vindo moço a multa sera de {} R$ e voce levara 4 pontos na carteira'.format(multa))
else:

    print('pó passar suave')