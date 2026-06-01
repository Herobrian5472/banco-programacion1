import random
n = int(input("Cantidad de numeros: "))

lista = []

for i in range(n):
    lista.append(random.randint(1,100))

def resultados():
    
    maximo = 0
    minimo = 10000
    contmax = 0
    contmin = 0
    
    for i in lista:
        if i > maximo:
            maximo = i
            contmax = 1
            
        elif i == maximo:
            contmax += 1 
            
        elif i < minimo:
            minimo = i
            contmin = 1
            
        elif i == minimo:
            contmin += 1
            
    print("Numeros: ", lista)
    print("Máximo: ", maximo)
    print("Contador de maximo: ", contmax)
    print("Minimo: ", minimo)
    print("Contador de minimo: ", contmin)
    
resultados()
    