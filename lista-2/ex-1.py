# -*- coding: utf-8 -*-

# Faça um Programa que peça os três lados de um triângulo.
# O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Digite o tamanho de um lado do triangulo: '))
b = int(input('Digite o tamanho de um lado do triangulo: '))
c = int(input('Digite o tamanho de um lado do triangulo: '))

if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um triangulo, pois um dos lados é maior que a soma dos \
        outros.')
elif a == b and b == c:
    print('É um triangulo equilátero.')
elif a == b or b == c or c == a:
    print('É um triangulo isósceles')
else:
    print('É um triangulo escaleno.')
