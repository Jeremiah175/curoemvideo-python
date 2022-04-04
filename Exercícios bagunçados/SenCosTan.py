'''import math
a = float(input('Digiete o angulo desejado em º: '))
print('O ângulo de {} tem o como Seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f}'.format(a,(math.sin(math.radians(a))),(math.cos(math.radians(a))),(math.tan(math.radians(a)))))'''

'''import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
print('O SENO de {} é {:.2f}'.format(ang,sen))
cos = math.cos(math.radians(ang))
print('O COSSENO de {} é {:.2f}'.format(ang,cos))
tang = math.tan(math.radians(ang))
print('A TANGENTE de {} é {:.2f}'.format(ang,tang))'''

from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
print('O SENO de {} é {:.2f}'.format(ang,sen))
cos = cos(radians(ang))
print('O COSSENO de {} é {:.2f}'.format(ang,cos))
tang = tan(radians(ang))
print('A TANGENTE de {} é {:.2f}'.format(ang,tang))




