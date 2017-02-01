def saqueTAA():

	valor = float(input("Digite o valor a ser sacado: ")) 

	notas50 = valor // 50
	valor = valor % 50 
	
	notas10 = valor // 10
	valor = valor % 10

	notas5 = valor//5
	valor = valor % 5

	notas1 = valor

	#%d usa pra modularizar	
	return "50.00 x %d;\n10.00 x %d;\n5.00 x %d;\n1.00 x %d" % (notas50,notas10,notas5,notas1) 
	#so usa esse retorno em strigns so em casos especificos, pois e melhor usa edd	
print(saqueTAA())