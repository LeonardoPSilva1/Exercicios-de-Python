print('-=-'*20)
print('analisando triangulo')
print('-=-'*20)

a = float(input("Lado a = "))
b = float(input("Lado b = "))
c = float(input("Lado c = "))

if a < b + c and b < a + c and c < a + b:
    print('os segumentos podem formar um triangulo', end=" ")
    if a == b == c:
        print('Equilatero!')
    elif a != b != c !=a:
        print('Escaleno! ')
    else:
        print('Isosceles!')
else:
    print('não pode formar um triangulo')
