from calendar import isleap
from datetime import date

ano = int(input('Digite o ano:'))
if ano == 0:
    ano = date.today().year

if isleap(ano):
    print('O ano {} É bissexto'.format(ano))
else:
    print('O ano {} Não é bissexto'.format(ano))