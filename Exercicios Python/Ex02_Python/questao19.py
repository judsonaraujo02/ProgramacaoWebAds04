def horaMinutoEmMinutos():
	
	horaDada= int(input("Digite a hora no formato HHMM: "))

	minutosPassados = ((horaDada//100)*60) + (horaDada%100)

	return "Passaram-se minutos: "+ str(minutosPassados)

print(horaMinutoEmMinutos( ))