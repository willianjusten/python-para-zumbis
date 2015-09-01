# -*- coding: utf-8 -*-

# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem
# do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Digite o valor do salario: '))
aumento = float(input('Digite o valor do aumento em porcentagem: '))

aumento_calculado = salario * aumento / 100
salario_calculado = salario + aumento_calculado

print('O valor do aumento é de R$ %.2f.' % aumento_calculado)
print('O novo salario é de R$ %.2f.' % salario_calculado)
