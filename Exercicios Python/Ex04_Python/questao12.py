def CalculaPrimo(num):

	divisores = 0
    i = 1
    
    while (i <= num):
        
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1

    if divisores == 2:
        return True
    else:
        return False

num = int(input("Digite o numero: ")) 

print(CalculaPrimo(num))
