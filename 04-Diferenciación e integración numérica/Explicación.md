# Explicación General — Diferenciación e Integración Numérica

En muchas situaciones reales no es posible obtener la derivada
o integral de una función de forma analítica. Esto ocurre cuando
la función es demasiado compleja, cuando solo se tienen datos
experimentales discretos o cuando la integral no tiene solución
en términos de funciones elementales.

Los métodos numéricos resuelven esto aproximando la derivada
o la integral usando los valores conocidos de la función en
puntos específicos llamados nodos.

## Diferenciación numérica
Se basa en aproximar la derivada usando diferencias entre
valores de la función en puntos cercanos. La precisión mejora
usando más puntos en la aproximación. En este tema se estudia
la regla de 3 y 5 puntos.

## Integración numérica
Se basa en aproximar el área bajo la curva usando figuras
geométricas simples como trapecios o parábolas. Entre más
subdivisiones se usen, mejor es la aproximación.

Existen dos enfoques principales:

### Métodos de Newton-Cotes
Usan puntos igualmente espaciados. Son simples de aplicar
pero menos eficientes. En este tema: Trapecio y Simpson.

### Métodos de cuadratura gaussiana
Usan puntos estratégicamente seleccionados para maximizar
la precisión con el mínimo número de evaluaciones.
En este tema: Cuadratura Gaussiana.