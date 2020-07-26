rept = 'S'
soma = 0
num = 0
maior = 0
menor = 0
while rept != 'N':
    number = int(input('Digite um número: '))
    soma += number
    num += 1
    if menor == 0:
        maior = number
        menor = number
    else:
        if number > maior:
            maior = number
        elif number < menor:
            menor = number
    rept = str(input('Deseja digitar mais algum número [S/N]? ')).upper()
media = soma / num
print('A média de todos os números juntos é {}.'.format(media))
print('O maior número digitado foi {}.'.format(maior))
print('E o menor número digitado foi {}.'.format(menor))