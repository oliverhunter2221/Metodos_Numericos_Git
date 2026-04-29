# Conceptos — Diferenciación e Integración Numérica

## ¿Qué es la diferenciación numérica?
Es el proceso de aproximar la derivada de una función usando
valores discretos conocidos de la función, sin necesidad de
obtener la derivada analítica. Se usa cuando la función es
muy compleja o solo se conocen datos experimentales.

## ¿Qué es la integración numérica?
Es el proceso de aproximar el valor de una integral definida
usando una suma finita de valores de la función. Se usa cuando
la integral no tiene solución analítica o cuando solo se
dispone de datos discretos.

## Conceptos clave

### Nodo
Punto donde se conoce o evalúa el valor de la función.

### Paso (h)
Distancia uniforme entre nodos consecutivos.
> h = (b - a) / n

### Error de truncamiento
Error introducido al aproximar una operación infinita
(derivada o integral) con un número finito de términos.

### Cuadratura
Término general para referirse a los métodos de integración
numérica. Proviene de la idea de aproximar el área bajo
una curva con figuras geométricas simples.

### Puntos de Gauss
Puntos especialmente seleccionados dentro del intervalo de
integración que minimizan el error de aproximación en la
cuadratura gaussiana.

### Polinomio de Legendre
Familia de polinomios usados para determinar los puntos y
pesos óptimos en la cuadratura gaussiana.