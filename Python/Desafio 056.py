anos = 0
fmenor = 0
velho = 0
name = str(0)
for c in range(0, 4):
    nome = str(input('Digite um nome: '))
    idade = int(input('Qual a sua idade? '))
    anos += idade
    print('''Qual o seu sexo?
            [ 1 ] Feminino
            [ 2 ] Masculino''')
    sexo = int(input('Qual a opção? '))
    if idade > velho:
        velho = idade
        name = nome
    if sexo == 1:
        if idade <= 20:
            fmenor += 1
midade = anos / 4
print('''A médida de idade das 4 pessoas é {} anos.
        Sendo o(a) mais velho(a) {}.
        ''')
if fmenor >= 1:
    print('Ainda temos {} mulher(res) abaixo dos 20 anos.')
else:
    print('Não tem nenhuma mulher abaixo dos 20 anos.')