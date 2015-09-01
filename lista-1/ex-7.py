# -*- coding: utf-8 -*-

# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

celsius = float(input('Digite a temperatura em Celsius: '))
print('A temperatura em Fahrenheit é de %.2f°F.' % ((9 * celsius) / 5 + 32))
