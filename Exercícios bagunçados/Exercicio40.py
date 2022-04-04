n1 = float(input('Qual foi a primeira nota: '))
n2 = float(input('Qual foi a segunda nota: '))
media = (n1 + n2) / 2
print('A média do aluno foi de {:.2f}'.format(media))
if media >= 70:
    print('Aluno APROVADO')
elif media < 70 and media >= 50:
    print('Aluno de RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')

