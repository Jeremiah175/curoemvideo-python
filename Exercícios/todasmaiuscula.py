n = str(input('Digite o seu  nome completo: '))
print('Seu nome em letras miúscula é: {}'.format(n.upper()))
print('Seu nome em letras minúscula é: {}'.format(n.lower()))
n1 = n.split()
n2 = ''.join(n1)
print('O número de letras sem espaço é: ', len(n2))
separa = n.split()
print('Seu primeiro nome tem: {} letras'.format(len(separa[0])))


'''n = str(input('Digite o seu  nome completo: ')).strip()
print('Seu nome em letras miúscula é: {}'.format(n.upper()))
print('Seu nome em letras minúscula é: {}'.format(n.lower()))
print('O número de letras sem espaço é: {}'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem: {}'.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome tem: {} letras'.format(len(separa[0])))'''



