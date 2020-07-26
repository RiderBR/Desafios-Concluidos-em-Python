from random import randint
computador = randint(0, 10) #Computador escolhe um número
palpites = 1
jogador = int(input('Em que número eu pensei? '))
while jogador != computador:
    jogador = int(input('Tente de novo. Em que número eu pensei? '))
    palpites += 1
print('VOCÊ ACERTOU! Pensei no número {}, você só teve que tentar {} vez(es).'.format(computador, palpites))
