s = int(input('Qual o número que deseja saber a tabuada? '))
for c in range(0, 11):
	m = s * c
	print('{} x {} = {}'.format(s, c, m))
	