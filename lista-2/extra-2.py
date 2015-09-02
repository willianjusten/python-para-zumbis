# -*- coding: utf-8 -*-

# Considere a empresa de telefonia Tchau.
# Abaixo de 200min, a empresa cobra 0.20 por minuto.
# Entre 200 e 400 min o preço é de 0.18. Acima de 400
# o preço é de 0.15. Calcule sua conta.
# Se o cliente usar mais de 800, paga tarifa de 0.08.

minutos = int(input('Digite a quantidade de minutos gastos: '))
if minutos < 200:
    preco = 0.20
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
print('O valor da conta é R$ %.2f' % (preco * minutos))
