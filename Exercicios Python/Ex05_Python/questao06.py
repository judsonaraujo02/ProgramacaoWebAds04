numeros=[]
pares=[]
impares=[]

for i in range(6):
  numero = int(input("Digite um numero :"))
  
  numeros.append(numero)
  
  if numero%2==0:
    pares.append(numero)
  else:
    impares.append(numero)
    
    
    
print(pares)
print(impares)
print(numeros)
  

