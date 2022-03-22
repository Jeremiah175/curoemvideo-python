p = float(input('Informe seu peso (Kg): '))
a = float(input('Informe sua altura (m): '))
imc = p / (a ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL')
elif 18.5 <= imc < 25:
    print('Você esta com PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE, procure um médico')
else:
    print('PROCURE UM MÉDICO URGENTE - OBSIDADE MÓRBIDA')
