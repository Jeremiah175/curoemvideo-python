a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar triâgulo')
else:
    print('Os segmentos acima NÃO formam triângulo')