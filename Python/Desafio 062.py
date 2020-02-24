primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = int(input('Quantos termos deseja saber? '))
num = 1
rept = 1
print('{} '.format(primeiro), end='→ ')
while rept == 1:
    while num != termo:
        primeiro = primeiro + razão
        print('{} '.format(primeiro), end='→ ')
        num += 1
    print('PAUSA')
    print('\nDeseja ver mais algum termo?'
          '\n[ 1 ] Sim'
          '\n[ 2 ] Não ')
    rept = int(input('Qual a sua escolha: '))
    if rept == 1:
        mais = int(input('Quantos termo mais deseja saber? '))
        termo = termo + mais
else:
    print('ACABOU')