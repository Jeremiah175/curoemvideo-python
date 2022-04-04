r = float(input('Quantos reais você tem? R$ '))
d = float(input('Qual a cotação atual do dolar (em R$)? '))
us = r/d
print()
print('Possui R$',r)
print('Cotação hoje USD',d)
print()
print('Com R$ {:.2f}, você conseguirá comprar USD {:.2f} !'.format(r,us))