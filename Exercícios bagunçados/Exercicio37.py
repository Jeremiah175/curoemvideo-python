n = int(input('Digite um número inteiro: '))
print('''Escolha uma opção de conversão:
[1] converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Qual a sua opção: '))
if opcao == 1:
    print('O número {} convertido em binário é {}'.format(n,bin(n)[2:]))
elif  opcao == 2:
    print('O número {} convertido em octal é {}'.format(n, oct(n)[2:]))
elif opcao == 3 :
    print('O número {} convertido em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')


