# Métodos — Diferenciación e Integración Numérica

## 1. Regla de 3 y 5 Puntos
Aproxima la derivada de una función usando 3 o 5 nodos
igualmente espaciados. Más puntos significan mayor precisión.

**Fórmula de 3 puntos (punto medio):**
> f'(x) ≈ (f(x+h) - f(x-h)) / 2h

**Fórmula de 5 puntos (punto medio):**
> f'(x) ≈ (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / 12h

**Ejemplo 1 — Situación resuelta:**
Un ingeniero aeronáutico necesita calcular la tasa de cambio
de la sustentación de un ala en función del ángulo de ataque.
Solo tiene mediciones en 3 ángulos consecutivos. Aplica la
regla de 3 puntos y obtiene una aproximación con error menor
al 0.01%.

**Ejemplo 2 — Situación resuelta:**
Un físico experimental mide la velocidad de una partícula
en 5 instantes de tiempo igualmente espaciados y necesita
calcular la aceleración en el punto central. Aplica la regla
de 5 puntos obteniendo mayor precisión que con 3 puntos.

**Ejemplo 3 — Situación no resuelta:**
Se intenta aplicar la regla de 3 puntos con un paso h muy
grande en una función que cambia rápidamente. El error de
truncamiento es tan grande que la aproximación de la derivada
es completamente incorrecta.

---

## 2. Método del Trapecio
Aproxima la integral dividiendo el área bajo la curva en
trapecios. Entre más subdivisiones se usen, mejor es la
aproximación.

**Fórmula simple:**
> ∫f(x)dx ≈ (h/2) × (f(a) + f(b))

**Fórmula compuesta:**
> ∫f(x)dx ≈ (h/2) × (f(x₀) + 2f(x₁) + 2f(x₂) + ... + f(xₙ))

**Ejemplo 1 — Situación resuelta:**
Un hidrólogo calcula el volumen de agua que pasa por una sección
de río durante 24 horas. Tiene mediciones de caudal cada hora.
Aplica la regla del trapecio compuesta con 24 subdivisiones
obteniendo el volumen con error menor al 2%.

**Ejemplo 2 — Situación resuelta:**
Un médico calcula la cantidad total de medicamento absorbido
por el cuerpo usando la curva de concentración en sangre medida
cada 30 minutos. La regla del trapecio compuesta da una buena
aproximación del área bajo la curva.

**Ejemplo 3 — Situación no resuelta:**
Se aplica la regla del trapecio simple con solo 2 puntos
a una función muy curva. La línea recta del trapecio no
representa bien la curva y el error es inaceptablemente grande.

---

## 3. Regla de Simpson
Aproxima la integral usando parábolas en lugar de líneas rectas,
obteniendo mayor precisión que el trapecio con el mismo número
de puntos. Requiere un número par de subintervalos.

**Fórmula de Simpson 1/3:**
> ∫f(x)dx ≈ (h/3) × (f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + f(xₙ))

**Fórmula de Simpson 3/8:**
> ∫f(x)dx ≈ (3h/8) × (f(x₀) + 3f(x₁) + 3f(x₂) + f(x₃))

**Ejemplo 1 — Situación resuelta:**
Un ingeniero mecánico calcula el trabajo realizado por una fuerza
variable sobre un pistón. Con 8 subdivisiones la regla de Simpson
1/3 da un error menor al 0.001% comparado con el valor exacto.

**Ejemplo 2 — Situación resuelta:**
Un astrónomo calcula la distancia recorrida por un cometa
integrando su velocidad variable a lo largo de su trayectoria.
Simpson 3/8 con 3 subintervalos da una excelente aproximación.

**Ejemplo 3 — Situación no resuelta:**
Se intenta aplicar Simpson 1/3 con un número impar de
subintervalos. La fórmula no puede aplicarse correctamente
y el resultado obtenido tiene un error significativo por
usar una fórmula incorrecta para el número de puntos disponibles.

---

## 4. Cuadratura Gaussiana
Selecciona estratégicamente los puntos de evaluación y sus
pesos para maximizar la precisión con el mínimo número de
evaluaciones. Es exacta para polinomios de grado 2n-1 usando
n puntos.

**Fórmula general:**
> ∫f(x)dx ≈ Σ wᵢ × f(xᵢ)

Donde xᵢ son los puntos de Gauss y wᵢ son los pesos asociados.

**Puntos y pesos para 2 puntos:**
> x = ±1/√3,  w = 1

**Puntos y pesos para 3 puntos:**
> x = 0, ±√(3/5),  w = 8/9, 5/9

**Ejemplo 1 — Situación resuelta:**
Un ingeniero nuclear calcula el flujo de neutrones en un reactor
integrando una función muy compleja. Con solo 3 puntos de Gauss
obtiene una precisión mayor que el trapecio con 100 subdivisiones.

**Ejemplo 2 — Situación resuelta:**
Un científico de materiales calcula la energía de deformación
de un material compuesto. La cuadratura gaussiana con 4 puntos
converge a la solución exacta ya que el integrando es un
polinomio de grado 7.

**Ejemplo 3 — Situación no resuelta:**
Se aplica cuadratura gaussiana estándar a una función con
una discontinuidad dentro del intervalo de integración.
Los puntos de Gauss no detectan la discontinuidad y el
resultado tiene un error muy grande. Se requiere dividir
el intervalo antes de aplicar el método.