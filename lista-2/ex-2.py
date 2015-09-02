# -*- coding: utf-8 -*-

# Determine se um ano é bissexto. Verifique no Google como fazer isso...
# Anos divisiveis por 4 são bissextos.
# Divisiveis por 100 não são.
# Mas divisiveis por 400 são.

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('É ano bissexto.')
else:
    print('Não é ano bissexto.')
