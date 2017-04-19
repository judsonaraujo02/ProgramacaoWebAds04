def ImpremeSomaMultde5(num):

	soma = 0
	for i in range(1,num,5):

		soma = soma + 5
		i = i+1
	print("Soma: ",soma)



num = int(input("Digite um numero postivo: "))
print(ImpremeSomaMultde5(num))
