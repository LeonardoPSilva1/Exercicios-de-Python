nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
nt3 = float(input('Digite a terceira nota: '))
nt4 = float(input('Digite a quarta nota: '))

calculo = (nt1 + nt2 + nt3 + nt4) / 4

print('Sua nota foi de {:.1f}'.format(calculo))

if 7 > calculo >= 5:
    print('Recuperção moço, F')
elif calculo < 5:
    print('É filho, foi de Foods and Drinks :(')
elif calculo > 7:
    print('Parabens meu nobre se passou suave')