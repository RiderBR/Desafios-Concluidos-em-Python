n1 = float(input('N1 do aluno: '))
n2 = float(input('N2 do aluno: '))
Nm = (n1 + n2) / 2
if Nm < 5.0:
    print('Média {}. REPROVADO. Estude mais ano que vem.'.format(Nm))
elif Nm >= 5.0 and Nm <= 6.9:
    print('Média {:.1f}. RECUPERAÇÂO. Estude mais.'.format(Nm))
else:
    print('Média {:.1f}. APROVADO, PARABÉNS!'.format(Nm))