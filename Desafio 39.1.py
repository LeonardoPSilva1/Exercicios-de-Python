from datetime import date
atual = date.today().year

print('''qual seu Genero: 
[ 1 ] Feminino 
[ 2 ] Masculino ''')

opção = int(input('Escolha uma das opções: '))

if opção == 1:
    print('Voce nn precisa se alistar')

elif opção == 2:
    print('vamos para o alistamento!')

    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    print(' Voce nasceu em {} tem {} anos'.format(ano,idade))

    if idade == 18:
        print(' VOCE SE ALISTA CACETE')

    elif idade < 18:
        saldo = 18 - idade
        print('Voce ainda nn tem 18, ainda faltam {} ano(s) para voce se alistar'.format(saldo))
        ano = atual + saldo

    elif idade > 18:
        saldo = idade - 18
        print('ja passou o seu tempo de se alisatar, voce deveria ter se alistado ha {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))









