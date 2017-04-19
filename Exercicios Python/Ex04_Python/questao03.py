def Imprime100NumPar(num):

	for i in range(num):
		if (i%2==0):
		print(i)
		i=i+1

num = int(input("Digite o numero do limite: "))

print(Imprime100NumPar(num))