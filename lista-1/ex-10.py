# -*- coding: utf-8 -*-

# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_dia = int(input('Quantos cigarros fuma por dia: '))
anos_fumante = float(input('Quantos anos já fumou: '))

num_cigarros_vida = cigarros_dia * (365 * anos_fumante)

print('O fumante perdeu %.2f dias de vida.' % (num_cigarros_vida * 10 / 1440))
