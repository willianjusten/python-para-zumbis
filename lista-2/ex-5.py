# -*- coding: utf-8 -*-

# Faça um Programa que leia três números e mostre o maior e o menor deles.

x = 0
maior = 0
menor = 10 ** 100
while x < 3:
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    x = x + 1
print('O maior numero é %d.' % maior)
print('O menor numero é %d.' % menor)
