from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu (AAAA): '))
idade  = atual - nasc
print('Quem nasceu em {} no ano {} tem {} anos'.format(nasc, atual, idade))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    print('Você ainda não tem 18 anos, faltam ainda {} anos para se alistar.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
elif idade > 18:
    print('Você ja deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(atual - (idade-18)))


