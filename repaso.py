import random

lista = []

for i in range(1,11):
    lista.append(i)
    
numero = random.choice(lista)

while True:
    
    num = int(input("Adivina el numero que estoy pensando del 1 al 10: "))
    
    if num == numero:
        print("felicitaciones, es el numero que pensaba.")
        break
    else:
        print("No es el numero.")
        continue