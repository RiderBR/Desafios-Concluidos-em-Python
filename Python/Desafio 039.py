from datetime import date
id = int(input('Qual o ano de seu nascimento? '))
ano = date.today().year
al = 18
ft = al - (ano - id)
if (ano - id) == al:
    print('Esta na hora de se apresentar a uma junta militar.')
elif (ano - id) < al:
    print('Ainda não está na hora de se apresentar. Falta {} anos.'.format(ft))
else:
    print('Passou {} anos de se apresentar. Vá a uma junta militar para regularizar seus status.'.format(ft))