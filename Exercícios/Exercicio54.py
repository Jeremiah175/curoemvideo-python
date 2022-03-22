from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pes)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas MENORES de idade'.format(totmenor))
