frase = str(input('Digite um frase ou palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1,-1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('A palavra ou frase digitada não forma um palindromo.')


