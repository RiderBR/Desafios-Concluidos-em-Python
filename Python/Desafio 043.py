al = float(input('Qual a sua altura em M? '))
pe = float(input('Qual o seu peso em Kg? '))
imc = pe / (al ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f}. Você está ABAIXO DO PESO normal.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}. Você está no seu PESO IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}. Você está com SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f}. Você está  com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))