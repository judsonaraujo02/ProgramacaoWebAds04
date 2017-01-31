qtdHoraNormal = float(input("Digite a quantidade de horas normais trabalhadas:  "))
qtdHoraExtra = float(input("Digite a quantidade de horas extras trabalhadas:  "))


salarioBruto = (qtdHoraNormal * 10) + (qtdHoraExtra * 15)
desconto = salarioBruto * 0.1
salarioLiquido = salarioBruto - desconto

print("Total a receber")
print("Valor do salario bruto:  ", salarioBruto)
print("Valor do salario liquido:  ",salarioLiquido)
