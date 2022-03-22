veloc = float(input('Qual a velocidade do veículo (km/h): '))
multa = int(7)
if veloc > 80:
    print('MULTADO!!! - Você ultrapassou o limite de velocidade da via de 80 km/h')
    print('Você recebeu uma multa de R$ {:.2f}'.format((veloc-80)*7))
print('Tenha um bom dia, dirija com segurança')
