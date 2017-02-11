def RecebeCorSinal(cor):

	if cor == "V":
		return "Siga!"

	elif cor ==  "A":
		return "Atenção!"
	else:
		return "Pare!"

cor = input("Digite uma das seguintes letras: V(verde), A(amarelo) e E(Vermelho):  ")
cor = cor.upper()

print(RecebeCorSinal(cor))
