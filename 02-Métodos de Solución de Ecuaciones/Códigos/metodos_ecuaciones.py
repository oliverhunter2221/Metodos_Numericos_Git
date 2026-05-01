# ============================================
# Tema 2: Métodos de Solución de Ecuaciones
# Métodos Numéricos
# ============================================

import math

# ---- Método 1: Newton-Raphson ----
print("=" * 40)
print("MÉTODO 1: NEWTON-RAPHSON")
print("=" * 40)

def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivada cero, método falla")
            return None
        x_nuevo = x - fx / dfx
        if abs(x_nuevo - x) < tolerancia:
            print(f"Convergió en {i+1} iteraciones")
            return x_nuevo
        x = x_nuevo
    print("No convergió")
    return None

# Ejemplo 1
print("\nEjemplo 1 - f(x) = x^2 - 2:")
f  = lambda x: x**2 - 2
df = lambda x: 2*x
raiz = newton_raphson(f, df, x0=1.0)
print(f"Raíz encontrada: {raiz}")

# Ejemplo 2
print("\nEjemplo 2 - f(x) = x^3 - x - 2:")
f2  = lambda x: x**3 - x - 2
df2 = lambda x: 3*x**2 - 1
raiz2 = newton_raphson(f2, df2, x0=1.5)
print(f"Raíz encontrada: {raiz2}")

# Ejemplo 3 - No resuelto (derivada cero)
print("\nEjemplo 3 - No resuelto (x0 con derivada cero):")
f3  = lambda x: x**3 - 2*x + 2
df3 = lambda x: 3*x**2 - 2
raiz3 = newton_raphson(f3, df3, x0=0.0)
print(f"Resultado: {raiz3}")

# ---- Método 2: Bisección ----
print("\n" + "=" * 40)
print("MÉTODO 2: BISECCIÓN")
print("=" * 40)

def biseccion(f, a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("No hay cambio de signo en el intervalo, método falla")
        return None
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tolerancia or (b - a) / 2 < tolerancia:
            print(f"Convergió en {i+1} iteraciones")
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Ejemplo 1
print("\nEjemplo 1 - f(x) = x^2 - 2 en [1, 2]:")
raiz = biseccion(lambda x: x**2 - 2, 1, 2)
print(f"Raíz encontrada: {raiz}")

# Ejemplo 2
print("\nEjemplo 2 - f(x) = x^3 - x - 2 en [1, 2]:")
raiz2 = biseccion(lambda x: x**3 - x - 2, 1, 2)
print(f"Raíz encontrada: {raiz2}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (sin cambio de signo):")
raiz3 = biseccion(lambda x: x**2 + 1, 1, 3)
print(f"Resultado: {raiz3}")

# ---- Método 3: Secante ----
print("\n" + "=" * 40)
print("MÉTODO 3: SECANTE")
print("=" * 40)

def secante(f, x0, x1, tolerancia=1e-6, max_iter=100):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1 - fx0) < 1e-12:
            print("División casi cero, método falla")
            return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tolerancia:
            print(f"Convergió en {i+1} iteraciones")
            return x2
        x0, x1 = x1, x2
    print("No convergió")
    return None

# Ejemplo 1
print("\nEjemplo 1 - f(x) = x^2 - 2:")
raiz = secante(lambda x: x**2 - 2, 1.0, 2.0)
print(f"Raíz encontrada: {raiz}")

# Ejemplo 2
print("\nEjemplo 2 - f(x) = x^3 - x - 2:")
raiz2 = secante(lambda x: x**3 - x - 2, 1.0, 2.0)
print(f"Raíz encontrada: {raiz2}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (puntos casi iguales):")
raiz3 = secante(lambda x: x**3 - x, 1.0, 1.0001)
print(f"Resultado: {raiz3}")

# ---- Método 4: Falsa Posición ----
print("\n" + "=" * 40)
print("MÉTODO 4: FALSA POSICIÓN")
print("=" * 40)

def falsa_posicion(f, a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("No hay cambio de signo en el intervalo, método falla")
        return None
    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        if abs(fc) < tolerancia:
            print(f"Convergió en {i+1} iteraciones")
            return c
        if fa * fc < 0:
            b = c
        else:
            a = c
    return c

# Ejemplo 1
print("\nEjemplo 1 - f(x) = x^2 - 2 en [1, 2]:")
raiz = falsa_posicion(lambda x: x**2 - 2, 1, 2)
print(f"Raíz encontrada: {raiz}")

# Ejemplo 2
print("\nEjemplo 2 - f(x) = x^3 - x - 2 en [1, 2]:")
raiz2 = falsa_posicion(lambda x: x**3 - x - 2, 1, 2)
print(f"Raíz encontrada: {raiz2}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (sin cambio de signo):")
raiz3 = falsa_posicion(lambda x: x**2 + 1, 1, 3)
print(f"Resultado: {raiz3}")