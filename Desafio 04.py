#Faça um programa que leia  algo pelo teclado e mostre na tela seu tipo primitivo
#e todas as informações sobre ela!

n = (input('Digite alguma coisa: '))

print('o tipo primitivo é: ', type(n))
print('Só tem espaço? ', n.isspace())
print('é um numero? ', n.isnumeric())
print('é alfabetico? ', n.isalpha())
print('é alfanumerico? ', n.isalnum())
print('Estão todos em letras maiusculas? ', n.isupper())
print('esta em minusculas? ', n.islower())


 

