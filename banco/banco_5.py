from datetime import datetime

#############################################
# LISTA DE USUARIOS CON SUS CONTRASEÑAS:
#############################################

usuarios = {
    "brian": {
        "clave": "777",
        "saldo": 44000
    },
    
    "tomy": {
        "clave": "888",
        "saldo": 50000
    },
    
    "juli": {
        "clave": "666",
        "saldo": 67000
    },
    
    "benja": {
        "clave": "555",
        "saldo": 71000
    },
    
    "ian": {
        "clave": "999",
        "saldo": 89999
    }
}


################################
# FUNCIONES
################################

# Función para registrar un nuevo usuario
def registrar_usuario():

    print("Los usuarios existentes son:\n")
    for usuario in usuarios:
        print(usuario)
    
    while True:
        nombre = input("\nIngrese un nuevo nombre de usuario: ")
        if nombre in usuarios:
            print("El usuario ya existe, intente con otro.")
            continue
        
        else:
            break
    
    while True:
        clave = input("Ingrese su contraseña por unica vez: ")
        confirma = input("Vuelva a escribir la contraseña: ")
                
        if clave != confirma:
            print("Las claves no coinciden, vuelva a intentarlo.")
            continue
        
        else:
            break
        
    monto = float(input("Ingrese el monto para iniciar en el banco: "))

    
    usuarios[nombre] = {
        "clave": clave,
        "saldo": monto
    }
    
    print("Los usuarios existentes son:\n")
    for usuario in usuarios:
        print(usuario)

# Función para eliminar un usuario
def eliminar_usuario():
    
    print("Los usuarios existentes son:\n")
    for usuario in usuarios:
        print(usuario)

    nombre = input("\nUsuario a eliminar: ")

    if nombre in usuarios:
        
        clave = input("Ingrese la contraseña del usuario: ")
        
        if clave == usuarios[nombre]["clave"]:
            del usuarios[nombre]
            print("Usuario eliminado.")
            
            print("Los usuarios existentes son:\n")
            for usuario in usuarios:
                print(usuario)
            
        else:
            print("Contraseña incorrecta. Usuario no eliminado.")
        
    else:
        print("Usuario no encontrado.")

# Funcion para login de usuario
def login():
    
    while True:

        
        user = input("Ingrese su nombre de usuario: ")
        if user in usuarios:
            break
        
        print("Usuario no existe.")

    while True:        
            
        clave = input("Ingrese su contraseña: ")
        
        if clave == usuarios[user]["clave"]:
            print("Datos ingresados correctamente.\n")
            return user
        
        print("Contraseña incorrecta, intente de nuevo.")

# Función para actualizar el saldo
def actualizar_saldo(usuario_actual, tipo, monto): 
    if tipo == "I":
        usuarios[usuario_actual]["saldo"] += monto
    elif tipo == "E":
        usuarios[usuario_actual]["saldo"] -= monto
    

'''
Hasta acá se crearon las funciones que vamos a usar en el menú de la siguiente version:
-Crear usuario
-Eliminar usuario
-Login
-Actualizar saldo

'''




#########################
# SE INICIA EL PROGRAMA
##########################
        
usuario_actual = login()

print("Bienvenido/a", usuario_actual,"\n")

saldo_inicial = usuarios[usuario_actual]["saldo"]

saldo = saldo_inicial

print("Su saldo actual es: ", saldo)


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
    
    #######################
    # Se cambia la funcion teniendo en cuenta el uso del diccionario, ahora opera sobre eso
    #######################
    saldo = actualizar_saldo(usuario_actual, tipo, monto)
    
    numero_operacion += 1
    
    # Guardar movimiento en la lista
    if tipo == "I":
        tipo = "Ingreso"
    elif tipo == "E":
        tipo = "Egreso"

    movimientos.append([numero_operacion, tipo, monto])


# Mostrar resultados finales
print("\n========== RESUMEN DE LA CUENTA ==========\n")

print("Usuario:\n", usuario_actual,"\n")

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
print("\nSaldo final:", usuarios[usuario_actual]["saldo"])
