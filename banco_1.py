from datetime import datetime

# Función para actualizar el saldo
def actualizar_saldo(saldo, tipo, monto):
    if tipo == "I":
        saldo += monto # saldo = saldo + monto
    elif tipo == "E":
        saldo -= monto
    return saldo


# Saldo inicial
saldo_inicial = float(input("Ingrese el saldo inicial: "))
saldo = saldo_inicial

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
    saldo = actualizar_saldo(saldo, tipo, monto)

    # Guardar movimiento en la lista
    if tipo == "I":
        tipo = "Ingreso"
    elif tipo == "E":
        tipo = "Egreso"
        
    numero_operacion += 1
    
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