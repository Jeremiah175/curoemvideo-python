n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Errei! Digitar valores correto
    [5] Sair''')
    opção = int(input('>>> Qual a opção desejada? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))
        continuar = str(input('Deseja fazer novamente [S/N]? ')).strip().upper()
        if continuar == 'S':
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
        elif continuar == 'N':
            continuar = 5
            opção = continuar
        else:
            print('\033[1;31mOpção inválida, por favor informar a opção novamente\033[m')
            continuar = str(input('Deseja fazer novamente [S/N]? ')).strip().upper()
            if continuar == 'S':
                n1 = float(input('Primeiro valor: '))
                n2 = float(input('Segundo valor: '))
            elif continuar == 'N':
                continuar = 5
                opção = continuar
    elif opção == 2:
        produto = n1 * n2
        print('O resultado da multiplicação entre {} x {} é igual a {}'. format(n1, n2, produto))
        continuar = str(input('Deseja fazer novamente [S/N]? ')).strip().upper()
        if continuar == 'S':
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
        elif continuar == 'N':
            continuar = 5
            opção = continuar
        else:
            print('\033[1;31mOpção inválida, por favor informar a opção novamente\033[m')
            continuar = str(input('Deseja fazer novamente [S/N]? ')).strip().upper()
            if continuar == 'S':
                n1 = float(input('Primeiro valor: '))
                n2 = float(input('Segundo valor: '))
            elif continuar == 'N':
                continuar = 5
                opção = continuar
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é o {}'.format(n1, n2, maior))
        continuar = str(input('Deseja fazer novamente [S/N]? ')).strip().upper()
        if continuar == 'S':
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo valor: '))
        elif continuar == 'N':
            continuar = 5
            opção = continuar
        else:
            print('\033[1;31mOpção inválida, por favor informar a opção novamente\033[m')
            continuar = str(input('Deseja fazer novamente [S/N]? ')).strip().upper()
            if continuar == 'S':
                n1 = float(input('Primeiro valor: '))
                n2 = float(input('Segundo valor: '))
            elif continuar == 'N':
                continuar = 5
                opção = continuar
    elif opção == 4:
        print('Informe os valores novamente!')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('\033[1;31mOpção inválida, por favor informar a opção novamente\033[m')
print('FIM DO PROGRAMA')
