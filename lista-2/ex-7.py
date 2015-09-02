# -*- coding: utf-8 -*-

# Faça um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#  e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total. Obs. : somente são vendidos um
# número inteiro de latas.

tam = int(input('Digite o tamanho em m2 que sera pintado: '))
if tam % 54 == 0:
    latas = tam / 54
else:
    latas = int(tam / 54) + 1

valor = latas * 80
print('São necessárias %d lata(s), que custa(m) R$ %.2f' % (latas, valor))
