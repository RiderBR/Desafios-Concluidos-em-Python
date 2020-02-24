number = int(input('Digite um número: '))
fatorial = 1
i = 2
while i <=  number:
    fatorial = fatorial * i
    i = i + 1
print('O fatorial de {} é {}.'.format(number, fatorial))