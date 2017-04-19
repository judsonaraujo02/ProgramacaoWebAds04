def questao07():
 
 notas = []
     
     for i in range(10):
         recebidas = [float(i) for i in input("Digite as notas do aluno (%d) separadas por espaço: " % (i+1)).split()]
         media = calcularMedia(recebidas)
         if(media >= 7.0):
             notas.append(media)
    print("O numero de alunos com nota acima da media (7.0) foi", len(notas))
 