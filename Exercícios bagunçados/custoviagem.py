'''dist = float(input('Qual a distância da viagem (km): '))
print('Sua viagem será de {:.2f} km'.format(dist))
if dist <= 200:
    print('E o preço da passagem será de R$ {:.2f}'.format(dist * 0.5))
else:
    print('E o preço da passagem será de R$ {:.2f}'.format(dist * 0.45))'''

dist = float(input('Qual a distância da viagem (km): '))
print('Sua viagem será de {:.2f} km'.format(dist))
if dist <= 200:
    preço = dist * 0.5
else:
    preço = dist * 0.45
print('E o preço da passagem será de R$ {:.2f}'.format(preço))