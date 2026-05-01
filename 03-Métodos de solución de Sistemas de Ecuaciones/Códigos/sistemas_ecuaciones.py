# ============================================
# Tema 3: Métodos de Solución de Sistemas
# de Ecuaciones
# Métodos Numéricos
# ============================================

# ---- Método 1: Eliminación Gaussiana ----
print("=" * 40)
print("MÉTODO 1: ELIMINACIÓN GAUSSIANA")
print("=" * 40)

def eliminacion_gaussiana(A, b):
    n = len(b)
    # Matriz aumentada
    M = [A[i][:] + [b[i]] for i in range(n)]
    
    for i in range(n):
        if M[i][i] == 0:
            print("Pivote cero, método falla")
            return None
        for j in range(i+1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n+1):
                M[j][k] -= factor * M[i][k]
    
    # Sustitución regresiva
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]
        for j in range(i+1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]
    return x

# Ejemplo 1
print("\nEjemplo 1 - Sistema 3x3:")
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]
sol = eliminacion_gaussiana(A, b)
print(f"Solución: x={sol[0]:.4f}, y={sol[1]:.4f}, z={sol[2]:.4f}")

# Ejemplo 2
print("\nEjemplo 2 - Sistema 3x3:")
A2 = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
b2 = [1, -2, 0]
sol2 = eliminacion_gaussiana(A2, b2)
print(f"Solución: x={sol2[0]:.4f}, y={sol2[1]:.4f}, z={sol2[2]:.4f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (pivote cero):")
A3 = [[0, 2, 1], [1, 0, 3], [2, 1, 0]]
b3 = [5, 10, 15]
sol3 = eliminacion_gaussiana(A3, b3)
print(f"Resultado: {sol3}")

# ---- Método 2: Gauss-Jordan ----
print("\n" + "=" * 40)
print("MÉTODO 2: GAUSS-JORDAN")
print("=" * 40)

def gauss_jordan(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    
    for i in range(n):
        if M[i][i] == 0:
            print("Pivote cero, método falla")
            return None
        pivot = M[i][i]
        for k in range(n+1):
            M[i][k] /= pivot
        for j in range(n):
            if j != i:
                factor = M[j][i]
                for k in range(n+1):
                    M[j][k] -= factor * M[i][k]
    
    return [M[i][n] for i in range(n)]

# Ejemplo 1
print("\nEjemplo 1 - Sistema 3x3:")
sol = gauss_jordan(A, b)
print(f"Solución: x={sol[0]:.4f}, y={sol[1]:.4f}, z={sol[2]:.4f}")

# Ejemplo 2
print("\nEjemplo 2 - Sistema 3x3:")
sol2 = gauss_jordan(A2, b2)
print(f"Solución: x={sol2[0]:.4f}, y={sol2[1]:.4f}, z={sol2[2]:.4f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (sistema dependiente):")
A3b = [[1, 2, 3], [2, 4, 6], [1, 1, 1]]
b3b = [6, 12, 4]
sol3 = gauss_jordan(A3b, b3b)
print(f"Resultado: {sol3}")

# ---- Método 3: Gauss-Seidel ----
print("\n" + "=" * 40)
print("MÉTODO 3: GAUSS-SEIDEL")
print("=" * 40)

def gauss_seidel(A, b, tolerancia=1e-6, max_iter=100):
    n = len(b)
    x = [0.0] * n
    for iteracion in range(max_iter):
        x_nuevo = x[:]
        for i in range(n):
            suma = sum(A[i][j] * x_nuevo[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        if all(abs(x_nuevo[i] - x[i]) < tolerancia for i in range(n)):
            print(f"Convergió en {iteracion+1} iteraciones")
            return x_nuevo
        x = x_nuevo
    print("No convergió")
    return x

# Ejemplo 1
print("\nEjemplo 1 - Sistema diagonal dominante:")
A_dd = [[10, 2, 1], [1, 10, 2], [2, 1, 10]]
b_dd = [13, 13, 13]
sol = gauss_seidel(A_dd, b_dd)
print(f"Solución: x={sol[0]:.4f}, y={sol[1]:.4f}, z={sol[2]:.4f}")

# Ejemplo 2
print("\nEjemplo 2 - Sistema diagonal dominante:")
A_dd2 = [[8, 1, 1], [1, 7, 2], [1, 2, 9]]
b_dd2 = [10, 10, 12]
sol2 = gauss_seidel(A_dd2, b_dd2)
print(f"Solución: x={sol2[0]:.4f}, y={sol2[1]:.4f}, z={sol2[2]:.4f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (no diagonal dominante):")
A_nd = [[1, 10, 2], [10, 1, 2], [2, 1, 1]]
b_nd = [13, 13, 4]
sol3 = gauss_seidel(A_nd, b_nd, max_iter=20)
print(f"Resultado: {sol3}")

# ---- Método 4: Jacobi ----
print("\n" + "=" * 40)
print("MÉTODO 4: JACOBI")
print("=" * 40)

def jacobi(A, b, tolerancia=1e-6, max_iter=100):
    n = len(b)
    x = [0.0] * n
    for iteracion in range(max_iter):
        x_nuevo = [0.0] * n
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        if all(abs(x_nuevo[i] - x[i]) < tolerancia for i in range(n)):
            print(f"Convergió en {iteracion+1} iteraciones")
            return x_nuevo
        x = x_nuevo
    print("No convergió")
    return x

# Ejemplo 1
print("\nEjemplo 1 - Sistema diagonal dominante:")
sol = jacobi(A_dd, b_dd)
print(f"Solución: x={sol[0]:.4f}, y={sol[1]:.4f}, z={sol[2]:.4f}")

# Ejemplo 2
print("\nEjemplo 2 - Sistema diagonal dominante:")
sol2 = jacobi(A_dd2, b_dd2)
print(f"Solución: x={sol2[0]:.4f}, y={sol2[1]:.4f}, z={sol2[2]:.4f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (no diagonal dominante):")
sol3 = jacobi(A_nd, b_nd, max_iter=20)
print(f"Resultado: {sol3}")