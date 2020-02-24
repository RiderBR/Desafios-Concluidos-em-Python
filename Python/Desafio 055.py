pm = 0
pn = 0
pb = 0
for c in range(0, 5):
    p = float(input('Digite aqui o seu peso em Kg: '))
    if p > pm:
        pm = p
    elif pn > p:
        pn = pn - p
        if pn < 0:
            pb = pn
print('O maior peso foi {:.2f}Kg e o menor foi {:.2f}Kg.'.format(pm, pb))