#crie um algoritmo que leia um numero e mostre seu dobre, triplo e raiz quadrada

n1 = int(input('Digite um Valor: '))
do = n1 * 2
tri = n1 * 3
r = pow(n1, 1/2)

print(' o dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n1, do, tri, r))