numeros = []

for i in range(1,5000):
    numeros.append(i)
    
no_multiplos = []

for i in numeros:
    if i % 3 == 0:
        continue
    
    else:
        no_multiplos.append(i)
        
print("Números del 1 al 5000 que no son múltiplos de 3:", no_multiplos)