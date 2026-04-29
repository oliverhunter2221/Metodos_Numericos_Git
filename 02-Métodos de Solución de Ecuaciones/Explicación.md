# Explicación General — Métodos de Solución de Ecuaciones

Cuando tenemos una ecuación no lineal como f(x) = 0 y no es posible
despejar x directamente, recurrimos a métodos numéricos iterativos.
Estos métodos parten de una aproximación inicial y van refinando
el resultado hasta llegar a un valor suficientemente cercano a la
raíz real.

Existen dos grandes familias de métodos:

## Métodos de intervalo (cerrados)
Requieren dos puntos iniciales a y b donde la función cambie de signo.
Garantizan encontrar la raíz si se cumplen las condiciones iniciales
pero convergen más lento. En este tema: Bisección y Falsa Posición.

## Métodos abiertos
Solo requieren uno o dos puntos iniciales sin necesidad de que
encierren la raíz. Convergen más rápido pero no siempre garantizan
encontrar la solución. En este tema: Newton-Raphson y Secante.

La elección del método depende de qué tanto sabemos sobre la función
y qué tan rápido necesitamos la solución.