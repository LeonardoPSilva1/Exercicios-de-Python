print('=======LOJA DO LEO=======')
compras = float(input('Preço das compras: '))

print('''Forma de pagamento: 
[ 1 ] á vista dinherio/cheque 
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ou mais''')

opção = int(input('Escolha uma das 4 opções: '))

if opção == 1:
    desconto = compras * 10 / 100
    resultado = compras - desconto

    print('Seu desconto foi de {} então suas compras ficaram {} R$'.format(desconto, resultado))

elif opção == 2:
    desconto = compras * 5 / 100
    resultado = compras - desconto

    print('Seu desconto foi de {} então suas compras ficaram {} R$'.format(desconto, resultado))

elif opção == 3:
    total = compras
    parcelas = compras / 2
    print('voce pagara 2x no cartão, então pagara: 2x de {:.2f}R$'.format(parcelas))
    print('Sua compra de {}R$ ficara {}R$'.format(compras, compras))

elif opção == 4:
    total =  compras + (compras * 20 / 100)
    totalpar = int(input('Quantas parcelas: '))

    parcela = total / totalpar

    print('sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalpar, parcela ))
    print('sua compra de R${:.2f} Vai custar R${} no final'.format(compras, total))

else:
    total = 0
    print('OPÇÃO INVALIDA')