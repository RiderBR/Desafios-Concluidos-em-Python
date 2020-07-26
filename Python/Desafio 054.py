from datetime import date
atual = date.today().year
m = 0
n = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    if atual - nasc > 21:
        m += 1
    else:
        n += 1
print('Das 7 pessoas, {} são maiores de 21 anos e {} ainda são menores de 21 anos.'.format(m, n))