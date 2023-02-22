from datetime import date

atual = date.today().year

ano = int(input('Em que ano voce nasceu? '))
idade = atual - ano

print('Voce tem {} anos!'.format(idade))

if idade <= 9:
    print('Classificação:  Mirim!')

elif idade <= 14:
    print('Classificação: Infantil!')

elif idade <= 19:
    print('Classificação: Junior!')

elif idade <= 25:
    print('Classificação: senior!')

elif idade >= 25:
    print('Voce é o master!!!!')