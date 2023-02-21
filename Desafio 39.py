from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Voce precisa se alistar!!!')
elif idade < 18:
    saldo =  18 - idade
    print('Voce ainda nn tem 18, ainda faltam {} ano(s) para voce se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('ja passou o seu tempo de se alisatar, voce deveria se alistar ha {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))