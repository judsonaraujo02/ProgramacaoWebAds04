def ImprimeQuadradoDosNum(num):

	for i in range(1,num+1):
		print(i*i)
		i=i+i

num = int(input("Digite o numero limite:")) 

print(ImprimeQuadradoDosNum(num))