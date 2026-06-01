import random

def maxmin(lista):
    
    cant_max = lista.count(max(lista))
    cant_min = lista.count(min(lista))
    return max(lista), cant_max, min(lista), cant_min

n = int(input("Cantidad de numeros: "))

ll = [random.randint(1,100) for valores in range(n)]

maximo, cont_max, minimo, cont_min = maxmin(ll)

print(maximo, cont_max, minimo, cont_min)