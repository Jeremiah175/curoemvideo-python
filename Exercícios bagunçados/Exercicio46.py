import emoji
from time import sleep
f = str(input('Acender Fogos [S/N]: '))
d = f.upper()
if d == 'N':
    print('COMEÇAR NOVAMENTE')
elif d == 'S':
    for c in range (10,-1,-1):
        print(c) #print(f'\b\b\b{c} ', end='', flush=True)
        sleep(0.6)
    print(emoji.emojize(':fireworks:', use_aliases=True))
else:
    print('OPÇÃO INVÁLIDA')

