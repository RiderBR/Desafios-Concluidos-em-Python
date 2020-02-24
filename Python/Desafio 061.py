primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = 0
print('{} '.format(primeiro), end='→ ')
while décimo != 9:
    primeiro = primeiro + razão
    print('{} '.format(primeiro), end='→ ')
    décimo += 1
print('ACABOU')

#Desafio parecido com o desafio 051