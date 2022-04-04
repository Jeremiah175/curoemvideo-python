from math import hypot
co = float(input('Qual a medida do Cateto Oposto, (cm): '))
ca = float(input('Qual a medida do Cateto Adjacente, (cm): '))
print('A hipotenusa será: {:.3f}'.format((hypot(co,ca))))