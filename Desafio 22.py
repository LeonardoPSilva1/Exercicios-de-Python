nome = str(input('Digite seu nome Completo: ')).strip()

print('Seu nome em maiusculo {}:'.format(nome.upper()))
print('Seu nome em minuscula é {}:'.format(nome.lower()))

print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


