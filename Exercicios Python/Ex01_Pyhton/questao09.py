sombraPessoa = float(input("Digite o valor da sombra da pessoa: "))
sombraPredio = float(input("Digite o valor da sombra do prédio:  "))
alturaPessoa = float(input("Digite o valor da altura da pessoa:  "))

sombraReal = (sombraPessoa/sombraPredio)
alturaPredio = (sombraReal*alturaPessoa)

print("A altura do prédio será:  ",alturaPredio)