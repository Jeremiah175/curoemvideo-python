from random import randint
from time import sleep
computador = randint(0,5) #faz o computador sortear um numero entre 0 e 5
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*18)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('PARABÉNS, VOCÊ ACERTOU')
else:
    print('ERROU!!!, eu pensei no número {} e não no {}'.format(computador,jogador))


