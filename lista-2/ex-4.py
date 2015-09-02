# -*- coding: utf-8 -*-

# Faça um Programa que leia três números e mostre o maior deles

x = 0
maior = 0
while x < 3:
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    x = x + 1
print('O maior numero é %d.' % maior)
