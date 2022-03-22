from tkinter import *
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[0;31; m= =\033[m' * 6)
print('''\033[0;31; m=\033[m  Suas opções:  \033[0;31; m=\033[m
\033[0;31; m=\033[m  [ 0 ] PEDRA   \033[0;31; m=\033[m
\033[0;31; m=\033[m  [ 1 ] PAPEL   \033[0;31; m=\033[m
\033[0;31; m=\033[m  [ 2 ] TESOURA \033[0;31; m=\033[m''')
print('\033[0;31; m= =\033[m' * 6)
jogador = int(input('\033[0;35; mQual é a sua jogada?\033[m '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PÔ!')
sleep(0.7)
print('-=' * 12)
print('Computador jogou {} '.format(itens[computador]))
print('Jogador jogou {} '.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!!')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA!')
