salario = float(input("Digite o salario do funcionario:  "))
conta1 = float(input("Digite o valor da conta 1:  "))
conta2 = float(input("Digite o valor da conta 2:  "))

multaConta1 = (conta1 * 0.02)+ conta1
multaConta2 = (conta2 * 0.02) + conta2

restoSalario= salario - (multaConta1 + multaConta2)

print("Valor da conta 1 com multa: ", multaConta1)
print("Valor da conta 2 com multa: ", multaConta2)

print("Valor que sobrará do salario: ", restoSalario)

