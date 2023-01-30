#desenvolva um programa que leia as 2 notas de um aluno e faça sua media

nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
nt3 = float(input('Digite a terceira nota: '))
nt4 = float(input('Digite a quarta nota: '))
r = (nt1 + nt2 + nt3 + nt4) / 4

print('A nota do aluno é igual a {:.1f}'.format(r))