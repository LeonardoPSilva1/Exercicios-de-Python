nome = str(input('Qual seu nome? '))
idade = int(input('Qual sua idade? '))

if idade < 18:
    print('Voce ainda nn precisa se alistar {}!'.format(nome))
elif idade == 18:
    print('Esta na hora de ir se Alistar {}!'.format(nome))
elif idade > 18:
    print('Ja passou do seu tempo de se alistar {}!'.format(nome))