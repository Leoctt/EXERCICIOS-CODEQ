A = float(input('valor de A: '))
B = float(input('Valor de B: '))
C = float(input('Valor de C: '))
pi = float(3.14159)
at = (A*C)/2
ac = pi*C**2
atr = ((A+B)*C)/2
aq = B*4
ar = A*B
print('Triângulo:{:.3f} \n Círculo:{:.3f} \n Trapézio:{:.3f} \n Quadrado:{:.3f} \n Retângulo{:.3f} '.format(at, ac, atr, aq, ar))