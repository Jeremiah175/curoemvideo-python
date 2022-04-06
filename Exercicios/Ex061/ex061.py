print('GERANDO UMA PA')
print('-+-' * 10)
primeiro = int(input('Qual o primeiro termo? '))
razão = int(input('Qual é a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razão
    cont += 1
print(' FIM')
