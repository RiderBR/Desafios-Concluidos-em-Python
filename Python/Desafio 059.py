n1 = int(input('Digite o primeiro número? '))
n2 = int(input('Digite o segundo número? '))
op = 0
while op != 5:
    print('''Escolha a opção desejada:
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos números
            [ 5 ] Sair do Programa''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}.\n'.format(n1, n2, soma))
    elif op == 2:
        multi = n1 * n2
        print('Os dois números {} e {} multiplicados dara um total de {}.\n'.format(n1, n2, multi))
    elif op == 3:
        if n1 > n2:
            print('O primeiro número digitado, {} é maior que o segundo, {}.\n'.format(n1, n2))
        else:
            print('O segundo número digitado, {} é maior que o {}.\n'.format(n2, n1))
    elif op == 4:
        n1 = int(input('\nDigite o primeiro novo número: '))
        n2 = int(input('\nDigite o segundo novo número: '))
print('Você saiu do programa!')
