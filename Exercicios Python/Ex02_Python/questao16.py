def areaQuadrado():
 	
	lado = float(input("Digite o valor do lado do quadrado: "))

	area = lado * 4
	perimetro = lado*lado

	return "A área do quadrado será: "+str(area)+ " e o perímetro será: "+str(perimetro)

print(areaQuadrado( ))
