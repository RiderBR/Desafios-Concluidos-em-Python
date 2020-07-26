VC = int(input('Qual o valor da casa? R$'))
T = int(input('Em quantos anos deseja pagar pela casa? '))
S = int(input('Qual o seu salario mensal? R$'))
T1 = T * 12
P = VC / T1
if P > (S * 0.3):
    print('Infelizmente seu financiamento foi negado.')
else:
    print('Seu financiamento foi aprovado. Seu financiamento ficou {}x'.format(T1), 'de R${:.6}.'.format(P))