print('-='*16)
print('Analizador de Triângulos v2.0')
print('-='*16)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILATERO!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Os segmentos PODEM FORMAR um triângulo ISOCELES!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')