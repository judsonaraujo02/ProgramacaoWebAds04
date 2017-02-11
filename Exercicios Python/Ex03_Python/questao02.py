def TesteIf(l1,l2,l3):

	letras = ''

	if l1 == 'V':
		letras = letras + 'A'

	else:	
		if l2 == 'V':
			if l3 == 'V':
				letras = letras +'B'

			else:
				letras = letras + 'C'
				letras = letras + 'D' 

	letras = letras + 'E'

	return letras

la = input("Digite uma letra: ")
lb = input("Digite uma letra: ")
lc = input("Digite uma letra: ")


print (TesteIf(la, lb, lc))