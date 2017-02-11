def RetornaMes(mes):

		if mes == 1:
			return "O mês é Janeiro!"
					
		if mes == 2:
			return "O mês é Fevereiro!"
						
		if mes == 3:
			return "O mês é Março!"

		if mes == 4:	
			return "O mês é Abril!"
					
		if mes == 5:	
			return "O mês é Maio!"

		if mes == 6:	
			return "O mês é Junho!"
					
		if mes == 7:	
			return "O mês é Julho!"	
					
		if mes == 8:	
			return "O mês é Agosto!"	
					
		if mes == 9:	
			return "O mês é Setembro!"	
					
		if mes == 10:
			return "O mês é Outubro!"
					
		if mes == 11:
			return "O mês é Novembro!"
				
		if mes == 12:	
			return "O mês é Dezembro!"

		else:
			return "Este número não corresponde a nenhum mês."	
	


mes = int(input("Digite o número do mês: "))

print(RetornaMes(mes))
