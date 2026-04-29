# Métodos — Solución de Ecuaciones

## 1. Método de Newton-Raphson
Parte de un punto inicial x₀ y usa la derivada de la función
para encontrar iterativamente la raíz. Es uno de los métodos
más rápidos cuando converge.

**Fórmula:**
> x₁ = x₀ - f(x₀) / f'(x₀)

**Ejemplo 1 — Situación resuelta:**
Un ingeniero necesita encontrar el diámetro exacto de una tubería
dado un caudal y una presión conocidos. La ecuación resultante
es no lineal. Aplicando Newton-Raphson con x₀ = 0.5 converge
a la solución en 4 iteraciones.

**Ejemplo 2 — Situación resuelta:**
Una empresa calcula la tasa de interés exacta de un préstamo
dado el monto y las cuotas mensuales. La ecuación financiera
no tiene solución directa. Newton-Raphson converge en 5 iteraciones
partiendo de x₀ = 0.1.

**Ejemplo 3 — Situación no resuelta:**
Se intenta encontrar la raíz de f(x) = x³ - 2x + 2 partiendo
de x₀ = 0. La derivada en ese punto es cero, causando división
entre cero y el método falla completamente.

---

## 2. Método de Bisección
Divide repetidamente el intervalo [a, b] a la mitad y selecciona
el subintervalo donde ocurre el cambio de signo, acercándose
progresivamente a la raíz.

**Fórmula:**
> c = (a + b) / 2

**Ejemplo 1 — Situación resuelta:**
Un arquitecto necesita encontrar el punto exacto donde una viga
curva cruza el nivel cero. Con f(a) < 0 y f(b) > 0 el método
de bisección encuentra la raíz en 20 iteraciones con tolerancia
de 0.0001.

**Ejemplo 2 — Situación resuelta:**
Un técnico calibra un sensor de temperatura buscando el valor
exacto donde la lectura es cero. Usando bisección en el intervalo
[-10, 10] converge a la solución en 15 iteraciones.

**Ejemplo 3 — Situación no resuelta:**
Se intenta aplicar bisección en el intervalo [1, 3] para f(x) = x² + 1.
Como f(1) = 2 y f(3) = 10 ambos son positivos, no hay cambio
de signo y el método no puede aplicarse porque no garantiza
la existencia de raíz en ese intervalo.

---

## 3. Método de la Secante
Similar a Newton-Raphson pero aproxima la derivada usando dos
puntos anteriores en lugar de calcularla directamente. No requiere
conocer la derivada analítica.

**Fórmula:**
> x₂ = x₁ - f(x₁) × (x₁ - x₀) / (f(x₁) - f(x₀))

**Ejemplo 1 — Situación resuelta:**
Un físico modela la trayectoria de un proyectil con una función
compleja cuya derivada es difícil de calcular. Usando la secante
con x₀ = 1 y x₁ = 2 encuentra la raíz en 6 iteraciones.

**Ejemplo 2 — Situación resuelta:**
Un químico busca la concentración exacta donde una reacción
llega al equilibrio. La función de equilibrio no tiene derivada
simple. La secante converge en 7 iteraciones.

**Ejemplo 3 — Situación no resuelta:**
Se aplica la secante con x₀ = 1 y x₁ = 1.0001 en una función
con raíz múltiple. f(x₁) - f(x₀) es tan pequeño que genera
división casi entre cero y el método diverge.

---

## 4. Método de Falsa Posición
Combina la seguridad del método de bisección con una mejor
estimación del punto medio usando una línea secante entre
los extremos del intervalo.

**Fórmula:**
> c = b - f(b) × (b - a) / (f(b) - f(a))

**Ejemplo 1 — Situación resuelta:**
Un hidrólogo busca el nivel exacto de agua en un canal donde
el caudal es cero. Con intervalo [0, 5] la falsa posición
converge más rápido que bisección encontrando la raíz en
10 iteraciones.

**Ejemplo 2 — Situación resuelta:**
Un mecánico encuentra el ángulo exacto donde la fuerza neta
sobre un mecanismo es cero. La falsa posición con intervalo
[0°, 90°] converge en 8 iteraciones.

**Ejemplo 3 — Situación no resuelta:**
Se aplica falsa posición en una función muy asimétrica donde
uno de los extremos del intervalo apenas cambia entre iteraciones.
El método converge extremadamente lento, necesitando cientos
de iteraciones para alcanzar la tolerancia requerida.