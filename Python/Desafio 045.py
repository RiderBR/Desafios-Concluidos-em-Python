import random
lista = ['Pedra', 'Papel', 'Tesoura']
print('-='*13)
print('''Escolha uma das opções:
    [ 1 ] - Pedra
    [ 2 ] - Papel
    [ 3 ] - Tesoura''')
print('-='*13)
jogador = int(input('Sua escolha: '))
print('-='*13)
print('Vez do computador.')
pc = random.choice(lista)
print('O computador escolheu {}.'.format(pc))
print('-='*13)
if jogador == 1:
    if pc == 'Pedra':
        print('EMPATE')
    elif pc == 'Tesoura':
        print('VOCÊ GANHOU')
    else:
        print('VOCÊ PERDEU.')
elif jogador == 2:
    if pc == 'Pedra':
        print('VOCÊ GANHOU')
    elif pc == 'Papel':
        print('EMPATE')
    else:
        print('VOCÊ PERDEU')
else:
    if pc == 'Pedra':
        print('VOCÊ PERDEU')
    elif pc == 'Papel':
        print('VOCÊ GANHOU')
    else:
        print('EMPATE')