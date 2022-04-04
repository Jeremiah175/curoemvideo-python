import random
n1 = str(input('Nome do Aluno 1: '))
n2 = str(input('Nome do Aluno 2: '))
n3 = str(input('Nome do Aluno 3: '))
n4 = str(input('Nome do Aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)