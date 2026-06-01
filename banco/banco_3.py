from datetime import datetime

# LISTA DE USUARIOS CON SUS CONTRASEÑAS:

usuarios = {
    "brian": "777",
    "tomy": "888",
    "juli": "666",
    "benja": "555",
    "ian": "999"
}

#############
#Tener en quenta que la llave (key) es el nombre de usuario, y la contraseña es el primer valor de esa llave (y el único en este caso)
#############
#ejemplo: si usas usuarios[tomy] te va a devolver 888.
###############


while True:

    
    user = input("Ingrese su nombre de usuario: ")
    if user in usuarios:
        break
    
    print("Usuario no existe.")

###################
# Otro WHILE para la contraseña, porque: hasta que no valide el usuario, no pedirá la contraseña.
#################

while True:        
        
    clave = input("Ingrese su contraseña: ")
    if clave == usuarios[user]: # Acá es donde usamos la llave para acceder a la contraseña
        print("Datos ingresados correctamente.\n")
        break
    
    print("Contraseña incorrecta, intente de nuevo.")
            

# Función para actualizar el saldo
def actualizar_saldo(saldo, tipo, monto): # con los parametros saldo, tipo, monto aun no definidos
    if tipo == "I":
        saldo += monto # saldo = saldo + monto
    elif tipo == "E":
        saldo -= monto
    return saldo


# Saldo inicial

while True: # Lo metimos en un bucle para poder usar el try en caso de que el usuario ingrese letras
    try:
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        saldo = saldo_inicial # si es correcto se vuelve saldo inicial
        break # y continua
    except:
        print("Debe ingresar un valor numérico.\n")
        


# Lista para guardar movimientos
movimientos = []

# Contador de operaciones
numero_operacion = 0

while True:
    tipo = input("Ingrese tipo de operación (I = ingreso, E = egreso o F = fin): ").upper()

    if tipo == "F":
        break

    if tipo != "I" and tipo != "E":
        print("Operación inválida.")
        continue

    monto = float(input("Ingrese el monto: "))

    # Llamada a la función
    saldo = actualizar_saldo(saldo, tipo, monto) # se llama a la funcion dentro de saldo para que al hacer return(resultado) lo agregue como valor de saldo, osea saldo = return de la funcion

    numero_operacion += 1

    
    # Guardar movimiento en la lista
    if tipo == "I":
        tipo = "Ingreso"
    elif tipo == "E":
        tipo = "Egreso"

    movimientos.append([numero_operacion, tipo, monto])
    
    
    


# Mostrar resultados finales
print("\n========== RESUMEN DE LA CUENTA ==========\n")

# Fecha actual
fecha_actual = datetime.now()
print("Fecha:", fecha_actual)

# Saldo inicial
print("Saldo inicial:", saldo_inicial)

# Listado de movimientos
print("\nMovimientos:")

for movimiento in movimientos:
    print(
        "Operación:", movimiento[0],
        "| Tipo:", movimiento[1],
        "| Monto:", movimiento[2]
    )

# Saldo final
print("\nSaldo final:", saldo)