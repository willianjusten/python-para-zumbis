# -*- coding: utf-8 -*-

# Calcule o fatorial de 10
# 10 * 9 * 8 * 7 ...

x = 10
fat = 1
while x > 0:
    fat = fat * x
    x = x - 1
print(fat)
