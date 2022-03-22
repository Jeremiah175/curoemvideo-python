n1 = float(input('Qual é o primeiro seguimento: '))
n2 = float(input('Qual é o segundo seguimento: '))
n3 = float(input('Qual é o terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os seguimentos informados NÃO PODEM FORMAR um triângulo.')
