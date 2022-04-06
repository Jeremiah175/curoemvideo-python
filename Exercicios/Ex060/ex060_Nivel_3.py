n = int(input('Qual número deseja saber o fatorial: '))
f = 1
print('{}! -> '.format(n), end='')
for c in range (n,f-1,-1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print(f)