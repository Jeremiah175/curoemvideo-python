print('=' * 26)
print('   10 TERMOS DE UMA PA   ')
print('=' * 26)
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range (p, decimo, r):
    print(c, end=' -> ')
print('ACABOU')