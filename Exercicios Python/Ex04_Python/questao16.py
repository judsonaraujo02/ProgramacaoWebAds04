
somaPares = 0
somaImpares = 0

for i in range(10):
    num = int(input("Digite um numero : "))
    if(num%2==0):
        somaPares = somaPares + 1
    else:
        somaImpares = somaImpares + 1
        
print("Total de numeros pares :",somaPares)
print("Total de numeros impares :",somaImpares)

