
def CalculaTempoPopAUltrapassarPopB(populacaoA, taxaA, populacaoB, taxaB):
   
    ano = 0
    
    while (populacaoA <= populacaoB):
       
        populacaoA = populacaoA * (1 + (taxaA/100))
        populacaoB = populacaoB * (1 + (taxaB/100))
        ano += 1 # ano = ano+1

    return ano


populacaoA = int(input("Digite a populacao de A: "))
taxaA = int(input("Digite a taxa de natalidade de A: "))

populacaoB = int(input("Digite a populacao de B: "))
taxaB = int(input("Digite a taxa de natalidade de B: "))

print(CalculaTempoPopAUltrapassarPopB(populacaoA,taxaA,populacaoB,taxaB))