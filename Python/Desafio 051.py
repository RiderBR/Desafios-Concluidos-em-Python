from time import sleep
n = int(input('Qual termo deseja saber? '))
a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual é a razão da PA? '))
an = a1 + (n - 1) * r
m = 1
print('-=' * 15)
print('Os 10 primeiros termos são:')
for c in range(0, 10):
    am = a1 + (m - 1) *r
    m += 1
    print(am)
    sleep(0.5)
print('-=' * 15)
print('O {}º termo é {}'.format(n, an))
