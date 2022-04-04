zona: str = input('Em qual zona pertence o terreno, (Norte=N, Sul=S, Leste=L e Oeste=O?)  ')
if zona=='n':
    print('O terreno localizado na Zona', zona.replace("n" , "Norte" , 8))
elif zona=='N':
    print('O terreno localizado na Zona', zona.replace("N" , "Norte" , 8))
elif zona == 's':
    print('O terreno localizado na Zona', zona.replace("s", "Sul", 8))
elif zona == 'S':
    print('O terreno localizado na Zona', zona.replace("S", "Sul", 8))
elif zona == 'l':
    print('O terreno localizado na Zona', zona.replace("l", "Leste", 8))
elif zona == 'L':
    print('O terreno localizado na Zona', zona.replace("L", "Leste", 8))
elif zona == 'o':
    print('O terreno localizado na Zona', zona.replace("o", "Oeste", 8))
elif zona == 'O':
    print('O terreno localizado na Zona', zona.replace("O", "Oeste", 8))
else:
    print('A opção de Zoneamento informado não é válido! Informar novamente!')
    exit()
lgar = float(input('Qual é a Largura da Garagem? '))
profgar = float(input('Qual é o Comprimento da Garagem? '))
areagaragem = lgar * profgar
lterreno = float(input('Qual é a largura do Terreno? '))
profterreno = float(input('Qual é o comprimento do Terreno? '))
areaterreno = lterreno * profterreno
percentual = ((areagaragem) / (areaterreno)) * 100
if zona=='n':
    print('O terreno está localizado na Zona', zona.replace("n" , "Norte" , 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona=='N':
    print('O terreno está localizado na Zona', zona.replace("N" , "Norte" , 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona == 's':
    print('O terreno está localizado na Zona', zona.replace("s", "Sul", 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona == 'S':
    print('O terreno está localizado na Zona', zona.replace("S", "Sul", 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona == 'l':
    print('O terreno está localizado na Zona', zona.replace("l", "Leste", 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona == 'L':
    print('O terreno está localizado na Zona', zona.replace("L", "Leste", 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona == 'o':
    print('O terreno está localizado na Zona', zona.replace("o", "Oeste", 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
elif zona == 'O':
    print('O terreno está localizado na Zona', zona.replace("O", "Oeste", 8),'e tem' ,round(percentual,2),'%','do coeficiente de aproveitamento')
else:
    print('A opção de Zoneamento informado não é válido! Informar novamente!')
print()
if zona=='N' and percentual<25:
    print('Projeto atende as Normas de Zonamento e do Plano Diretor')
elif zona=='L' or zona=='W' and percentual<=30:
    print('Projeto atende as Normas de Zonamento e do Plano Diretor')
elif zona=='S' and percentual<=40:
    print('Projeto atende as Normas de Zonamento e do Plano Diretor')
else:
    print('REVISAR AS MEDIDAS - O PROJETO NÃO ATENDE O PLANO DIRETOR DE ZONEAMENTO DESTE MUNICÍPIO!')
