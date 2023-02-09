from time import sleep

viagem = float(input('Digite quantos é a distancia da sua viagem em KM: '))
print('sua viagem é de {}KM'.format(viagem))

print('PROCESSANDO PREÇO DA VIAGEM....')
sleep(3)

preço = viagem * 0.50 if  viagem <=200 else viagem * 0.45


'''if viagem <=200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45'''

print('Sua passagem ficou {:.2f}R$'.format(preço))