s = 0
c = int
for c in range(1, 500):
    if c % 3 == 0:
        s += c
print('A soma de todos os multiplos de 3 de 1 a 500 é {}.'.format(s))