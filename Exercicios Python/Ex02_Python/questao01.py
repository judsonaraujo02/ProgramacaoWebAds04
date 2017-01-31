def Mensagem():

	x = 10
	y = 1
	x -= 1
	y += 2
	x = x - 1
	y = y + 2
	x= x-1
	y = y+2

	return " x= " + str(x) + " e y= "+str(y)

print(Mensagem() ) 

def DemoFuncao(b):
	a= (b * 2)
	b= b+5
	c= a-b
	return "a = %d; b = %d; c = %d" % (a,b,c)

print(DemoFuncao(0))
print(DemoFuncao(5))
print(DemoFuncao(10))
print(DemoFuncao(15))
print(DemoFuncao(20))

