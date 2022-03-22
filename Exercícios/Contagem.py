import time
print('Contagem regressiva')
for i in range (10,-1,-1):
    print(f'\b\b\b{i} ', end='', flush=True)
    time.sleep(0.5)