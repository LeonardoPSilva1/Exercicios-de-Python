a = int(input('Digite um numero: '))
b = int(input('Digite outro numero:  '))
c = int(input('Digite outro numero: '))

'verificar menor'
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('o menor valor é: {}'.format(menor))

'verificando o maior'
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('o maior valor é: {}'.format(maior))
