# ============================================
# Tema 1: Errores de Programación
# Métodos Numéricos
# ============================================

# ---- Error 1: Redondeo Binario ----
print("=" * 40)
print("ERROR 1: REDONDEO BINARIO")
print("=" * 40)

# Ejemplo 1 - Resuelto
print("\nEjemplo 1 - Resuelto:")
precio = 0.10
total = precio * 3
print(f"Total sin redondeo: {total}")
total_redondeado = round(total, 2)
print(f"Total con round(): {total_redondeado}")

# Ejemplo 2 - Resuelto
print("\nEjemplo 2 - Resuelto:")
temperatura = 0.0
for i in range(10):
    temperatura += 0.1
print(f"Temperatura acumulada sin redondeo: {temperatura}")
print(f"Temperatura con round(): {round(temperatura, 2)}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto:")
balance = 0.0
for i in range(1000):
    balance += 0.01
print(f"Balance acumulado (con error): {balance}")
print(f"Balance esperado: {1000 * 0.01}")

# ---- Error 2: Comparación con == ----
print("\n" + "=" * 40)
print("ERROR 2: COMPARACIÓN DIRECTA CON ==")
print("=" * 40)

# Ejemplo 1 - Resuelto
print("\nEjemplo 1 - Resuelto:")
saldo = 0.1 + 0.2
esperado = 0.3
epsilon = 0.001
if abs(saldo - esperado) < epsilon:
    print(f"Saldo correcto usando tolerancia epsilon")
else:
    print(f"Saldo incorrecto")

# Ejemplo 2 - Resuelto
print("\nEjemplo 2 - Resuelto:")
x = 0.1 + 0.2
objetivo = 0.3
if abs(x - objetivo) < 1e-9:
    print("Coordenada alcanzada con tolerancia")
else:
    print("Coordenada no alcanzada")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto:")
presion = 0.1 + 0.2
if presion == 0.3:
    print("Válvula abierta")
else:
    print(f"Válvula no abre: presion={presion} != 0.3")

# ---- Error 3: Acumulación en Bucles ----
print("\n" + "=" * 40)
print("ERROR 3: ACUMULACIÓN DE ERRORES EN BUCLES")
print("=" * 40)

# Ejemplo 1 - Resuelto
print("\nEjemplo 1 - Resuelto:")
h = 0.1
n = 1000
tiempo_correcto = h * n
print(f"Tiempo correcto (multiplicación): {tiempo_correcto}")

# Ejemplo 2 - No resuelto
print("\nEjemplo 2 - No resuelto:")
tiempo_acumulado = 0.0
for i in range(1000):
    tiempo_acumulado += 0.1
print(f"Tiempo acumulado (con error): {tiempo_acumulado}")
print(f"Diferencia: {abs(tiempo_acumulado - tiempo_correcto)}")