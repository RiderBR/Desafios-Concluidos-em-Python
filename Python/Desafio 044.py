price = float(input('Digite o valor do produto: R$'))
print('-='*28)
print(''''Escolha uma forma de pagamento:
      [ 1 ] Á vista (Dinheiro/Cheque)
      [ 2 ] Á Vista no Cartão
      [ 3 ] 2x no Cartão
      [ 4 ] 3x ou mais''')
print('-='*28)
op = int(input('Sua opção: '))
print('-='*28)
if op == 1:
    pricef = price - (price * 0.1)
    print('O valor a ser pago sera de R${:.2f}, com 10% de desconto.'.format(pricef))
elif op == 2:
    pricef = price - (price * 0.05)
    print('O valor a ser pago sera de R${:.2f}, com 5% de desconto.'.format(pricef))
elif op == 3:
    print('O valor a ser pago sera de R${:.2f}, sem desconto'.format(price))
elif op == 4:
    pricef = price + (price * 0.2)
    print('O valor a ser pago sera de R${:.2f}, com 20% de juros.'.format(pricef))
else:
    print('Opção Incorreta.')