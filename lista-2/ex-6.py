# -*- coding: utf-8 -*-

# Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário
# bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
# Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

val_hora = float(input('Digite o quanto ganha por hora: '))
horas_mes = int(input('Digite qtd de horas trabalhadas no mês: '))

salario_bruto = val_hora * horas_mes

desc_ir = salario_bruto * 0.11
desc_inss = salario_bruto * 0.08
desc_sind = salario_bruto * 0.05
salario_liquido = salario_bruto - desc_ir - desc_inss - desc_sind

print('Salario Bruto: R$ %.2f' % salario_bruto)
print('Desconto IR: R$ %.2f' % desc_ir)
print('Desconto INSS: R$ %.2f' % desc_inss)
print('Desconto Sindicato: R$ %.2f' % desc_sind)
print('Salario Líquido: R$ %.2f' % salario_liquido)
