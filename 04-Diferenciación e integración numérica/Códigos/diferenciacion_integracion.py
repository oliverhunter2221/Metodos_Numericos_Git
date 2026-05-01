# ============================================
# Tema 4: Diferenciación e Integración Numérica
# Métodos Numéricos
# ============================================

import math

# ---- Método 1: Regla de 3 y 5 Puntos ----
print("=" * 40)
print("MÉTODO 1: REGLA DE 3 Y 5 PUNTOS")
print("=" * 40)

def tres_puntos(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def cinco_puntos(f, x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

# Ejemplo 1
print("\nEjemplo 1 - Derivada de sin(x) en x=pi/4:")
f = math.sin
x = math.pi / 4
h = 0.1
derivada_exacta = math.cos(x)
derivada_3p = tres_puntos(f, x, h)
print(f"Valor exacto:    {derivada_exacta:.6f}")
print(f"Regla 3 puntos:  {derivada_3p:.6f}")
print(f"Error:           {abs(derivada_exacta - derivada_3p):.6f}")

# Ejemplo 2
print("\nEjemplo 2 - Derivada de x^3 en x=2:")
f2 = lambda x: x**3
x2 = 2.0
h2 = 0.01
derivada_exacta2 = 3 * x2**2
derivada_5p = cinco_puntos(f2, x2, h2)
print(f"Valor exacto:    {derivada_exacta2:.6f}")
print(f"Regla 5 puntos:  {derivada_5p:.6f}")
print(f"Error:           {abs(derivada_exacta2 - derivada_5p):.6f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (h muy grande):")
h_grande = 10.0
derivada_mala = tres_puntos(math.sin, math.pi/4, h_grande)
print(f"Derivada con h=10: {derivada_mala:.6f}")
print(f"Error grande:      {abs(derivada_exacta - derivada_mala):.6f}")

# ---- Método 2: Regla del Trapecio ----
print("\n" + "=" * 40)
print("MÉTODO 2: REGLA DEL TRAPECIO")
print("=" * 40)

def trapecio(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return (h / 2) * suma

# Ejemplo 1
print("\nEjemplo 1 - Integral de sin(x) en [0, pi]:")
resultado = trapecio(math.sin, 0, math.pi, 100)
exacto = 2.0
print(f"Valor exacto:   {exacto:.6f}")
print(f"Trapecio n=100: {resultado:.6f}")
print(f"Error:          {abs(exacto - resultado):.6f}")

# Ejemplo 2
print("\nEjemplo 2 - Integral de x^2 en [0, 1]:")
resultado2 = trapecio(lambda x: x**2, 0, 1, 1000)
exacto2 = 1/3
print(f"Valor exacto:     {exacto2:.6f}")
print(f"Trapecio n=1000:  {resultado2:.6f}")
print(f"Error:            {abs(exacto2 - resultado2):.6f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (n=2 en función muy curva):")
resultado3 = trapecio(math.sin, 0, math.pi, 2)
print(f"Trapecio n=2:  {resultado3:.6f}")
print(f"Error grande:  {abs(exacto - resultado3):.6f}")

# ---- Método 3: Regla de Simpson ----
print("\n" + "=" * 40)
print("MÉTODO 3: REGLA DE SIMPSON")
print("=" * 40)

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        print("n debe ser par para Simpson 1/3")
        return None
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * f(a + i * h)
        else:
            suma += 4 * f(a + i * h)
    return (h / 3) * suma

def simpson_38(f, a, b):
    h = (b - a) / 3
    return (3 * h / 8) * (f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))

# Ejemplo 1
print("\nEjemplo 1 - Integral de sin(x) en [0, pi] con Simpson 1/3:")
resultado = simpson_13(math.sin, 0, math.pi, 100)
print(f"Valor exacto:      {exacto:.6f}")
print(f"Simpson 1/3 n=100: {resultado:.6f}")
print(f"Error:             {abs(exacto - resultado):.6f}")

# Ejemplo 2
print("\nEjemplo 2 - Integral de x^3 en [0, 1] con Simpson 3/8:")
resultado2 = simpson_38(lambda x: x**3, 0, 1)
exacto2 = 0.25
print(f"Valor exacto:   {exacto2:.6f}")
print(f"Simpson 3/8:    {resultado2:.6f}")
print(f"Error:          {abs(exacto2 - resultado2):.6f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (n impar en Simpson 1/3):")
resultado3 = simpson_13(math.sin, 0, math.pi, 3)
print(f"Resultado: {resultado3}")

# ---- Método 4: Cuadratura Gaussiana ----
print("\n" + "=" * 40)
print("MÉTODO 4: CUADRATURA GAUSSIANA")
print("=" * 40)

def cuadratura_gaussiana(f, a, b, n=3):
    # Puntos y pesos para n=2 y n=3
    puntos_pesos = {
        2: [(-1/math.sqrt(3), 1), (1/math.sqrt(3), 1)],
        3: [(-math.sqrt(3/5), 5/9), (0, 8/9), (math.sqrt(3/5), 5/9)]
    }
    if n not in puntos_pesos:
        print("Solo se soporta n=2 o n=3")
        return None
    pp = puntos_pesos[n]
    resultado = 0
    for xi, wi in pp:
        t = ((b - a) * xi + (a + b)) / 2
        resultado += wi * f(t)
    return resultado * (b - a) / 2

# Ejemplo 1
print("\nEjemplo 1 - Integral de sin(x) en [0, pi] con 3 puntos:")
resultado = cuadratura_gaussiana(math.sin, 0, math.pi, n=3)
print(f"Valor exacto:          {exacto:.6f}")
print(f"Cuadratura 3 puntos:   {resultado:.6f}")
print(f"Error:                 {abs(exacto - resultado):.6f}")

# Ejemplo 2
print("\nEjemplo 2 - Integral de x^3 en [0, 1] con 2 puntos:")
resultado2 = cuadratura_gaussiana(lambda x: x**3, 0, 1, n=2)
exacto2 = 0.25
print(f"Valor exacto:          {exacto2:.6f}")
print(f"Cuadratura 2 puntos:   {resultado2:.6f}")
print(f"Error:                 {abs(exacto2 - resultado2):.6f}")

# Ejemplo 3 - No resuelto
print("\nEjemplo 3 - No resuelto (función con discontinuidad):")
def f_discontinua(x):
    if x == 0:
        return 0
    return 1 / x

try:
    resultado3 = cuadratura_gaussiana(f_discontinua, -1, 1, n=3)
    print(f"Resultado con discontinuidad: {resultado3:.6f}")
    print("El resultado es incorrecto por la discontinuidad en x=0")
except Exception as e:
    print(f"Error: {e}")