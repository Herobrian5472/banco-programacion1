import random

def resultados(lista):
    
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
            
    return maximo, contmax, minimo, contmin

n = int(input("Cantidad de numeros: "))

lista = []

for i in range(n):
    lista.append(random.randint(1,100))
    
print(lista,"\n")
    
maximo, contmax, minimo, contmin = resultados(lista)

print(f'Maximo: {maximo} \nContador de maximo: {contmax} \nMinimo: {minimo} \nContador de minimo: {contmin}')