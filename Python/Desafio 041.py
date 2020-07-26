from datetime import date
id = int(input('Em que ano você nasceu? '))
ano = date.today().year
categoria = ano - id
if categoria <= 9:
    print('Idade: {} anos. Categoria Mirim.'.format(categoria))
elif categoria <= 14:
    print('Idade: {} anos. Categoria Infantil'.format(categoria))
elif categoria <= 19:
    print('Idade: {} anos. Categoria Junior.'.format(categoria))
elif categoria < 25:
    print('Idade: {} anos. Categoria Sênior'.format(categoria))
else:
    print('Idade: {} anos. Categoria Master.'.format(categoria))