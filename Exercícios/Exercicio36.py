valor = float(input('Qual é o valor da casa a ser financiada? R$ '))
salario = float(input('Qual seu atual salário? R$ '))
anos = int(input('Em quantos anos pretende quitar o empréstimo? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.0f} em {} anos a prestação será de R$ {:.2f} por mês'.format(valor, anos, prestacao))
if prestacao > minimo:
    print('EMPRÉSTIMO \033[0;30;41mNEGADO\033[m')
else:
    print('EMPRÉSTIMO \033[0;30;32mCONCEDIDO\033[m')


