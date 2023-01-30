#Crie um programa que leia o quanto de dinheiro ela tem e mostre o quanto de dolares ela pode comprar.

r = float(input('Quando de dinheiro voce tem em reais? '))
d = r / 5.11

print('O dolar hoje é de 5,11 US$, voce tem {} então pode comprar {:.2f} US$'.format(r, d))
