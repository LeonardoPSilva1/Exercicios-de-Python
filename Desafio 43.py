peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura*altura)

print('Seu peso é de {} e voce tem {:.2f} de altura, então seu IMC é: {:.1f}'.format(peso, altura, IMC))

if IMC <= 18.5:
    print('Abaixo do Peso normal, CUIDADOO!')
elif 18.5 <= IMC < 25:
    print('Seu peso é normal!')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('obesidade')
elif IMC > 40:
    print('Mae do Renan')