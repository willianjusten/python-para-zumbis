# -*- coding: utf-8 -*-

# Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar

mercadoria = float(input('Insira o preço da mercadoria: '))
desconto = float(input('Insira o valor do desconto: '))

desconto_calculado = mercadoria * desconto / 100
valor_final = mercadoria - desconto_calculado

print('O valor do desconto é de R$ %.2f.' % desconto_calculado)
print('Valor a pagar R$ %.2f.' % valor_final)
