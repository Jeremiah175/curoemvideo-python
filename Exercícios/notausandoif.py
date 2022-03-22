n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a seguda nota? '))
m = (n1+n2)/2
print('* Sua MÉDIA FINAL foi de: {:.2f} *'.format(m))
if m<6.0:
    print('Você não passou direto')
else:
    print('Parabéns você foi APROVADO')

