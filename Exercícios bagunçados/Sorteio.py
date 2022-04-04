'''import random
lista = input('Nome do primeiro Aluno: '),\
        input('Nome do segundo Aluno: '),\
        input('Nome do terceiro Aluno: '),\
        input('Nome do quarto Aluno: ')
print('Quem irá apagar o quadro é: {}'.format(random.choice(lista)))'''

import random
n1 = str(input('Nome do Aluno 1: '))
n2 = str(input('Nome do Aluno 2: '))
n3 = str(input('Nome do Aluno 3: '))
n4 = str(input('Nome do Aluno 4: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

