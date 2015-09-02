# -*- coding: utf-8 -*-

# Imprima as tabuadas de 1 a 10

tab = 1
while tab <= 10:
    x = 1
    print('\nTabuada de %d' % tab)
    while x <= 10:
        print('%d x %d = %d' % (tab, x, tab * x))
        x = x + 1
    tab = tab + 1
