def Mensagem():

	x = 10
	y = 1
	x -= 1 #x=x-1
	y += 2 #y=y+2
	x = x-1
	y = y+2
	x = x-1
	y = y+2

	if x > y: # if = se
		
		return "X ficou maior que Y"
	
	elif x < y: #elif = senao se
		
		return "X ficou menor que Y"	

	else: # else =senao
		
		return " X e Y ficaram iguais"

print(Mensagem())