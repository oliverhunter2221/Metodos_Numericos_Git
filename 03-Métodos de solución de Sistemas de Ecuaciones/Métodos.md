# Métodos — Solución de Sistemas de Ecuaciones

## 1. Eliminación Gaussiana
Transforma el sistema original en un sistema triangular superior
mediante operaciones de fila, luego resuelve por sustitución
regresiva de abajo hacia arriba.

**Ejemplo 1 — Situación resuelta:**
Un ingeniero civil calcula las fuerzas en 3 nodos de una estructura
metálica. El sistema de 3 ecuaciones se resuelve aplicando
eliminación gaussiana, obteniendo las fuerzas en cada nodo
mediante sustitución regresiva.

**Ejemplo 2 — Situación resuelta:**
Un nutricionista formula una dieta con 3 alimentos que debe
cumplir exactamente con calorías, proteínas y carbohidratos.
El sistema 3x3 se resuelve con eliminación gaussiana encontrando
la cantidad exacta de cada alimento.

**Ejemplo 3 — Situación no resuelta:**
Se intenta resolver un sistema donde al aplicar eliminación
gaussiana aparece un cero en la posición del pivote y no hay
filas disponibles para intercambiar. El método falla por
división entre cero sin aplicar pivoteo parcial.

---

## 2. Método de Gauss-Jordan
Extiende la eliminación gaussiana eliminando elementos tanto
por debajo como por encima del pivote, obteniendo directamente
la matriz identidad y la solución sin necesidad de sustitución
regresiva.

**Ejemplo 1 — Situación resuelta:**
Un economista resuelve un modelo de equilibrio de mercado con
3 productos interdependientes. Gauss-Jordan transforma la matriz
aumentada hasta obtener la identidad, dando directamente
los precios de equilibrio de cada producto.

**Ejemplo 2 — Situación resuelta:**
Un ingeniero eléctrico calcula las corrientes en 4 ramas de
un circuito usando las leyes de Kirchhoff. Gauss-Jordan resuelve
el sistema de 4 ecuaciones obteniendo cada corriente directamente.

**Ejemplo 3 — Situación no resuelta:**
Se aplica Gauss-Jordan a un sistema de ecuaciones linealmente
dependientes. Al reducir la matriz aparece una fila de puros
ceros indicando que el sistema tiene infinitas soluciones
y no hay una solución única.

---

## 3. Método de Gauss-Seidel
Método iterativo que actualiza cada incógnita usando los valores
más recientes disponibles de las demás incógnitas en cada iteración.

**Fórmula general:**
> xᵢ = (bᵢ - Σaᵢⱼxⱼ) / aᵢᵢ

**Ejemplo 1 — Situación resuelta:**
Una red eléctrica de distribución con 100 nodos necesita calcular
los voltajes en cada punto. Gauss-Seidel converge en 25 iteraciones
usando la diagonal dominante de la matriz de admitancias.

**Ejemplo 2 — Situación resuelta:**
Un simulador de temperatura en una placa metálica divide la placa
en una malla de puntos. Gauss-Seidel calcula la temperatura en
cada punto iterando hasta que los cambios son menores a 0.001°C.

**Ejemplo 3 — Situación no resuelta:**
Se aplica Gauss-Seidel a un sistema cuya matriz no es diagonal
dominante. Las aproximaciones oscilan y se alejan de la solución
en cada iteración, el método diverge y nunca converge.

---

## 4. Método de Jacobi
Método iterativo similar a Gauss-Seidel pero actualiza todas
las incógnitas simultáneamente usando solo los valores de la
iteración anterior, no los recién calculados.

**Fórmula general:**
> xᵢ⁽ᵏ⁺¹⁾ = (bᵢ - Σaᵢⱼxⱼ⁽ᵏ⁾) / aᵢᵢ

**Ejemplo 1 — Situación resuelta:**
Un procesador de imágenes aplica un filtro de suavizado a cada
pixel de una fotografía. Jacobi actualiza todos los pixeles
simultáneamente en cada iteración convergiendo en 30 iteraciones.

**Ejemplo 2 — Situación resuelta:**
Un modelo climático calcula la presión atmosférica en una malla
de puntos geográficos. Jacobi permite paralelizar el cálculo
ya que todas las incógnitas se actualizan al mismo tiempo,
convergiendo en 40 iteraciones.

**Ejemplo 3 — Situación no resuelta:**
Se aplica Jacobi a un sistema mal condicionado donde los elementos
fuera de la diagonal son mayores que los de la diagonal. El método
diverge desde las primeras iteraciones alejándose cada vez más
de la solución real.