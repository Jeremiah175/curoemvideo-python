nome = str(input('Qual é o seu nome? '))
if nome == 'Wilson':
    print('Seu nome é lindo!!!')
elif nome == 'José' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bíblico e muito comum!')
elif nome == 'Creuza' or nome == 'Godofredo':
    print('Eca, que nome é esse?!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}'.format(nome))