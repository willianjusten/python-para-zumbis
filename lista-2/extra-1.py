# -*- coding: utf-8 -*-

# Considere a empresa de telefonia Tchau.
# Abaixo de 200min, a empresa cobra 0.20 por minuto.
# Entre 200 e 400 min o preço é de 0.18. Acima de 400
# o preço é de 0.15. Calcule sua conta.

minutos = int(input('Digite a quantidade de minutos gastos: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos <= 400:
        preco = 0.18
    else:
        preco = 0.15
print('O valor da conta é R$ %.2f' % (preco * minutos))
