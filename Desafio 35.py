print('-=-'*20)
print('analisando triangulo')
print('-=-'*20)

a = float(input("Lado a = "))
b = float(input("Lado b = "))
c = float(input("Lado c = "))

if a < b + c and b < a + c and c < a + b:
    print('os segumentos podem formar um triangulo')
else:
    print('não pode formar um triangulo')






















'''if (a < b + c and b < a + c and c <  b +c):
    if (a == b and b == c):
        print("\nOs lados formam um Triângulo Equilátero.")
    else:
        if (a == b or a == c or b == c):
            print("\nOs lados formam um Triângulo Isósceles.")
        else:
            print("\nOs lados formam um Triângulo Escaleno.")
else:
    print("\nOs lados não formam um triângulo!")

sair = input("\nDigite ENTER para sair...")'''