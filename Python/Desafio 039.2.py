from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('''Qual o seu sexo? 
        [ 1 ] Masculino
        [ 2 ] Feminino''')
sexo = int(input('R: '))
idade = atual - nasc
if sexo == 1:
    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será {}'.format(ano))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('No seu caso o alistamento não é obrigatorio, mais sim uma opção.')