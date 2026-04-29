# Explicación General — Métodos de Solución de Sistemas de Ecuaciones

Cuando tenemos un sistema de varias ecuaciones con varias incógnitas,
resolverlo a mano se vuelve impráctico. Los métodos numéricos nos
permiten encontrar la solución de forma sistemática y eficiente.

Existen dos grandes familias de métodos para sistemas de ecuaciones:

## Métodos directos
Obtienen la solución exacta en un número finito de operaciones
aplicando transformaciones algebraicas a la matriz del sistema.
Son ideales cuando el sistema no es muy grande y se necesita
precisión. En este tema: Eliminación Gaussiana y Gauss-Jordan.

## Métodos iterativos
Parten de una aproximación inicial y refinan la solución en cada
iteración hasta alcanzar la tolerancia deseada. Son ideales para
sistemas muy grandes donde los métodos directos serían demasiado
costosos computacionalmente. En este tema: Gauss-Seidel y Jacobi.

La elección del método depende del tamaño del sistema, la estructura
de la matriz y la precisión requerida. Para sistemas pequeños se
prefieren los métodos directos. Para sistemas grandes y dispersos
se prefieren los iterativos.