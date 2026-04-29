# Conceptos — Métodos de Solución de Sistemas de Ecuaciones

## ¿Qué es un sistema de ecuaciones?
Un sistema de ecuaciones es un conjunto de dos o más ecuaciones
con dos o más incógnitas que deben satisfacerse simultáneamente.
En métodos numéricos se trabaja principalmente con sistemas lineales
de la forma Ax = b donde A es una matriz de coeficientes, x es
el vector de incógnitas y b es el vector de términos independientes.

## Conceptos clave

### Matriz de coeficientes (A)
Arreglo rectangular de números que representa los coeficientes
de las incógnitas en cada ecuación del sistema.

### Vector de términos independientes (b)
Vector que contiene los valores del lado derecho de cada ecuación.

### Matriz aumentada [A|b]
Combinación de la matriz A y el vector b usada para aplicar
operaciones de fila durante la solución.

### Pivote
Elemento de la diagonal principal usado como referencia para
eliminar los demás elementos de su columna.

### Diagonal dominante
Una matriz es diagonal dominante cuando el valor absoluto del
elemento de la diagonal es mayor que la suma de los valores
absolutos del resto de elementos de esa fila. Es una condición
importante para garantizar la convergencia de los métodos iterativos.

### Convergencia en sistemas
Los métodos iterativos convergen cuando las aproximaciones
sucesivas del vector x se acercan cada vez más a la solución exacta.