n = int(input('Qual número deseja saber o fatorial: '))
c = n
f = 1
print('Calculando {}! -> '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c = c - 1
print('{}'.format(f))