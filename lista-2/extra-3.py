# -*- coding: utf-8 -*-

# Imprima os numeros pares entre 0 e um numero
# fornecido usando if

num = int(input('Digite um numero: '))
x = 0
while x <= num:
    if x % 2 == 0:
        print(x)
    x = x + 1
